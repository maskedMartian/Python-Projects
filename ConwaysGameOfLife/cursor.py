# cursor manipulation module

import sys
import os
import ctypes
from ctypes import c_long, c_wchar_p, c_ulong, c_void_p

if os.name == 'nt':
    import msvcrt
    import ctypes

#classes
class _CursorInfo(ctypes.Structure):
    _fields_ = [("size", ctypes.c_int), ("visible", ctypes.c_byte)]

#functions
def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

# ==============================================================================    

def moveCursor(x, y):
   handle = ctypes.windll.kernel32.GetStdHandle(c_long(-11))
   position = x + (y << 16)
   ctypes.windll.kernel32.SetConsoleCursorPosition(handle, c_ulong(position))

# ==============================================================================

def hideCursor():
    if os.name == 'nt':
        info = _CursorInfo()
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(info))
        info.visible = False
        ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(info))
    elif os.name == 'posix':
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()

# ==============================================================================

def showCursor():
    if os.name == 'nt':
        info = _CursorInfo()
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(info))
        info.visible = True
        ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(info))
    elif os.name == 'posix':
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()
