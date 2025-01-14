"""
Example script for Calculator on Windows 10

Requirements:
  - Windows 10
  - pywinauto 0.6.1+

Win10 version of Calculator is very specific. Few different processes (!)
own different windows and controls, so the full hierarchy can be accessed
through Desktop object only.

Minimized Calculator is a process in a "Suspended" state.
But it can be restored with some trick for invisible main window.
"""

from pywinauto import Desktop, Application


app = Application(backend="uia").start('calc.exe')
app.click_input(coords=(23,12))

# dlg = Desktop(backend="uia").计算器
# dlg.type_keys('2*3=')
# app.print_control_identifiers()

# dlg.minimize()
# Desktop(backend="uia").window(name='计算器', visible=None).restore()
