# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['mainDodges.py'],
    pathex=[],
    binaries=[],
    datas=[('./assets/accept.png', 'assets'), ('assets/ban.png', 'assets'), ('assets/rune.png', 'assets'), ('assets/close.png', 'assets'), ('assets/search.png', 'assets'), ('assets/None.png', 'assets'), ('assets/bangrey.png', 'assets'), ('assets/PickAChampion.png', 'assets'), ('assets/autoFillJgl.png', 'assets'), ('assets/close1.png', 'assets'), ('assets/BanAChamp.png', 'assets'), ('assets/decline.png', 'assets')],
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
