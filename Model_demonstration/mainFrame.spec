# -*- mode: python -*-

block_cipher = None


a = Analysis(['mainFrame.py'],
             pathex=['H:\\ML Project\\Model demonstration'],
             binaries=[],
             datas=[('car_data.txt', '.'), ('lasso_model.pickle', '.'), ('ols_model.pickle', '.')],
             hiddenimports=['cython','sklearn','sklearn.ensemble','sklearn.neighbors.typedefs','sklearn.neighbors.quad_tree','sklearn.tree._utils','scipy._lib.messagestream', 'statsmodels.tsa.statespace._filters'],
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
          [],
          exclude_binaries=True,
          name='mainFrame',
          debug=True,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='mainFrame')
