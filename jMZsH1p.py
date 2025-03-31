import ctypes
from win32api import *
from win32con import *
from win32gui import *
from win32ui import *
from random import randrange

x = 1920
y = 1080

while True:
    dc = GetDC(0)
    StretchBlt(dc, 0, 0, x, y, dc, -20, -20, x+40, y+40, SRCCOPY)
    DeleteDC(dc)