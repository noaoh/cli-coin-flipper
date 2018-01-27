#!/usr/bin/python3
# Cursor code based on https://stackoverflow.com/questions/5174810/how-to-turn-off-blinking-cursor-in-command-window

import sys
import os

if os.name == 'nt':
    import msvcrt
    import ctypes

    class _CursorInfo(ctypes.Structure):
        _fields_ = [("size", ctypes.c_int), ("visible", ctypes.c_byte)]

def hide_cursor():
    if os.name == 'nt':
        ci = _CursorInfo()
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.GetConsoleCursorInfo(handle,\
                ctypes.byref(ci))
        ci.visible = False
        ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))

    elif os.name == 'posix':
        sys.stdout.write("\e?25l")
        sys.stdout.flush()



def show_cursor():
    if os.name == 'nt':
        ci = _CursorInfo()
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
        ci.visible = True
        ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))

    elif os.name == 'posix':
        os.system('setterm -cursor on')
        sys.stdout.write("\e?25h")
        sys.stdout.flush()

def clear_screen():
    if os.name == 'nt':
        os.system('cls')

    elif os.name == 'posix':
        os.system('clear')
