# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['src\\main.py'],
    pathex=['src'],
    binaries=[],
    datas=[
        ('src', 'src'),
        ('src/static/graal.ico', 'src/static')
    ],
    hiddenimports=[
        'mysql', 
        'mysql.connector', 
        'src',

        'database',
        'database.database',

        'domain', 
        'domain.venda', 
        'domain.item', 
        
        'controller', 
        'controller.venda_controller', 
        'controller.produto_controller',

        'model',
        'model.produto_model',
        'model.venda_model',

        'view',
        'view.app',
        'view.caixa_eletronico_view',
        'view.controle_estoque_view',
        'view.widgets',
        'view.widgets.botao',
        'view.widgets.etiqueta',
        'view.widgets.input',
        'view.widgets.tabela',
    ],
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
    name='sistema_graal',
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
    icon=['src\\static\\graal.ico'],
)
