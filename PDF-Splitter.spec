# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['PDF-Splitter.py'],
    pathex=[],
    binaries=[],
    datas=[('scribe-logo-final.webp', '.'), ('C:/Users/Scribe/AppData/Local/Programs/Python/Python313/Lib/site-packages/tkinterdnd2', 'tkinterdnd2'), ('scribe-icon.ico', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='PDF Splitter',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['scribe-icon.ico'],
)
