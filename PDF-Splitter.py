import os
import threading
from tkinter import filedialog, messagebox
import customtkinter as ctk
from tkinterdnd2 import TkinterDnD, DND_FILES
from PyPDF2 import PdfReader, PdfWriter
from PIL import Image
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def split_pdf(file_path, results, index):
    """
    Splits a PDF file into two bins: Bin 1 (pages 1-500) and Bin 2 (pages 501-1000).
    Saves the output files with the bin numbers appended to the original file name.
    """
    try:
        reader = PdfReader(file_path)
        bin1_writer = PdfWriter()
        bin2_writer = PdfWriter()

        for i in range(len(reader.pages)):
            if i < 500:
                bin1_writer.add_page(reader.pages[i])
            elif i < 1000:
                bin2_writer.add_page(reader.pages[i])

        file_name, file_ext = os.path.splitext(os.path.basename(file_path))
        output_dir = os.path.dirname(file_path)

        bin1_path = os.path.join(output_dir, f"{file_name}_Bin1{file_ext}")
        with open(bin1_path, "wb") as output_file:
            bin1_writer.write(output_file)

        bin2_path = os.path.join(output_dir, f"{file_name}_Bin2{file_ext}")
        with open(bin2_path, "wb") as output_file:
            bin2_writer.write(output_file)

        results[index] = f"Processed: {bin1_path}, {bin2_path}"
    except Exception as e:
        results[index] = f"Error processing file '{file_path}': {str(e)}"

def process_multiple_files(file_paths):
    threads = []
    results = [None] * len(file_paths)

    for i, file_path in enumerate(file_paths):
        thread = threading.Thread(target=split_pdf, args=(file_path, results, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    success_files = [res for res in results if res and "Error" not in res]
    error_files = [res for res in results if res and "Error" in res]

    if success_files:
        messagebox.showinfo("Success", f"Processed files:\n" + "\n".join(success_files))
    if error_files:
        messagebox.showwarning("Errors", f"Failed to process the following files:\n" + "\n".join(error_files))

def select_files():
    file_paths = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
    if file_paths:
        process_multiple_files(file_paths)

def drop_event(event):
    raw_file_paths = event.data.strip()
    file_paths = raw_file_paths.split("} {")
    cleaned_file_paths = []

    for path in file_paths:
        normalized_path = os.path.normpath(path.strip().strip("{}"))
        if os.path.isfile(normalized_path):
            cleaned_file_paths.append(normalized_path)

    if cleaned_file_paths:
        process_multiple_files(cleaned_file_paths)
    else:
        messagebox.showwarning("Invalid Input", "No valid PDF files were provided.")

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = TkinterDnD.Tk()
app.title("PDF Splitter")
app.geometry("400x300")
app.iconbitmap(resource_path("scribe-icon.ico"))

logo_image = ctk.CTkImage(
    light_image=Image.open(resource_path("scribe-logo-final.webp")),
    dark_image=Image.open(resource_path("scribe-logo-final.webp")),
    size=(200, 100),
)

logo_label = ctk.CTkLabel(app, image=logo_image, text="")
logo_label.pack(pady=(10, 30))

frame = ctk.CTkFrame(app, width=400, height=200, corner_radius=15, fg_color="#FFA500")
frame.pack(pady=(0, 20))

drag_drop_label = ctk.CTkLabel(
    frame,
    text="Drag & Drop Files to Upload\n\nOR",
    font=ctk.CTkFont(size=16, weight="bold"),
    text_color="gray",
)
drag_drop_label.pack(pady=20, padx=20)

browse_button = ctk.CTkButton(
    frame,
    text="Browse Files",
    command=select_files,
    width=150,
    height=40,
    corner_radius=8,
    font=ctk.CTkFont(size=16, weight="bold"),
)
browse_button.pack(pady=10)

app.drop_target_register(DND_FILES)
app.dnd_bind("<<Drop>>", drop_event)

app.mainloop()