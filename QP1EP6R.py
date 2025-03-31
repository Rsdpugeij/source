import ctypes
from win32api import *
from win32con import *
from win32gui import *
from win32ui import *
from random import randrange

# You can remove the message box part since you don't want any message boxes

x = 1920  # Width
y = 1080  # Height

def tunnel():
    dc = GetDC(0)
    StretchBlt(dc, 0, 0, x, y, dc, -20, -20, x+40, y+40, SRCCOPY)
    DeleteDC(dc)

for i in range(100):
    tunnel()
