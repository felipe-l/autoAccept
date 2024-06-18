# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['mainDodges.py'],
    pathex=[],
    binaries=[],
    datas=[('assets/accept.png', '.'), ('assets/ban.png', '.'), ('assets/rune.png', '.'), ('assets/close.png', '.'), ('assets/search.png', '.'), ('assets/None.png', '.'), ('assets/bangrey.png', '.'), ('assets/PickAChampion.png', '.'), ('assets/autoFillJgl.png', '.'), ('assets/close1.png', '.'), ('assets/BanAChamp.png', '.'), ('assets/decline.png', '.')],
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
    name='mainDodges',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon="./interLogo.png",
)
