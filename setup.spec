# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['printcalculator\\gui.py'],
             pathex=['D:\\RepositoriosGIT\\3Dprinter_calculator\\printcalculator', 'D:\\RepositoriosGIT\\3Dprinter_calculator'],
             binaries=[],
             datas=[('printcalculator\\config.ini', '.'), ('printcalculator\\calculadora.ico', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='3D_cost_calculator',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
	  upx_exclude=[],
	  runtime_tmpdir=None,
          console=False, icon='printcalculator\\calculadora.ico' )
