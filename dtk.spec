# -*- mode: python -*-
a = Analysis(['dtk.pyw'],
             pathex=['T:\\Projects\\Deskside Tool Kit\\Semi Stable\\v1.1\\TestDir'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
			 
a.datas += [('YO.png', 'YO.png',  'DATA')]
a.datas += [('spreadsheet.xlsx', 'spreadsheet.xlsx',  'DATA')]
a.datas += [('spreadsheetcrypt.xlsx', 'spreadsheetcrypt.xlsx',  'DATA')]
a.datas += [('spreadsheetnew.xlsx', 'spreadsheetnew.xlsx',  'DATA')]
a.datas += [('spreadsheetready.xlsx', 'spreadsheetready.xlsx',  'DATA')]
             
			 
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='dtk.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True , icon='icon.ico')
