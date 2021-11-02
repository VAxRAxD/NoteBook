import cx_Freeze
import os
import sys
base=None

if sys.platform == 'win32':
    base='Win32GUI'

os.environ['TCL_LIBRARY']=r"C:\Users\Admin\AppData\Local\Programs\Python\Python39\tcl\tcl8.6"
os.environ['TK_LIBRARY']=r"C:\Users\Admin\AppData\Local\Programs\Python\Python39\tcl\tk8.6"

executables=[cx_Freeze.Executable("app.py",base=base,icon='media/main/Notebook.ico')]

cx_Freeze.setup(
    name = "Notebook",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["media/main/Notebook.ico",'tcl86t.dll','tk86t.dll', 'media']}},
    version = "1.1",
    description = "Tkinter Application",
    executables = executables
    )