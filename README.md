# PDF Splitter

PDF Splitter is a desktop application that allows users to split large PDF files into two separate bins based on page ranges. It provides an intuitive drag-and-drop interface, file browsing, and is built using Python with the CustomTkinter library.

## Features

- **Drag-and-Drop Support:** Easily drag and drop files into the application for processing.
- **Multi-File Processing:** Handles multiple PDFs at once using multithreading for faster processing.
- **Clean Interface:** Built with CustomTkinter, featuring a modern, user-friendly design.
- **PDF Splitting:** Automatically splits PDFs into two bins:
  - **Bin 1:** Pages 1–500.
  - **Bin 2:** Pages 501–1000.
- **Icon and Branding:** Custom app logo and icon included for a polished appearance.

## Requirements

- **Python 3.7 or newer**
- Libraries:
  - `customtkinter`
  - `tkinterdnd2`
  - `PyPDF2`
  - `Pillow`

## Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/pdf-splitter.git
    cd pdf-splitter
    ```

2. **Install Dependencies:** Use pip to install the required Python libraries:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application:**

    ```bash
    python PDF-Splitter.py
    ```

## Usage

### Running the Application
- Launch the application.
- Drag and drop PDF files into the interface or click "Browse Files" to select them.
- The application will process the files, splitting them into two bins based on page ranges.

### Packaged Executable
If you're using the pre-built executable:
1. Download the `.exe` file from the Releases page.
2. Double-click the file to launch the application.

### Building the Executable
To create a standalone executable, follow these steps:

1. **Install PyInstaller:**

    ```bash
    pip install pyinstaller
    ```

2. **Build the Executable:**

    ```bash
    pyinstaller --onefile --noconsole --icon=scribe-icon.ico --add-data "scribe-logo-final.webp;." PDF-Splitter.py
    ```

3. **Find the Executable:** The built file will be located in the `dist` directory.

## Files Included

- `PDF-Splitter.py`: Main script.
- `scribe-icon.ico`: Application icon.
- `scribe-logo-final.webp`: Logo displayed in the GUI.
- `requirements.txt`: Dependencies for the project.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request for review.

## License

This project is licensed under the MIT License.

## Acknowledgments

- **CustomTkinter:** For the modern GUI design.
- **TkinterDnD2:** For enabling drag-and-drop functionality.
- **PyPDF2:** For handling PDF operations.