import os
import win32api,win32con
from win32gui import *
from win32api import *
from win32ui import *
from win32con import *
from random import *
import ctypes
import sys

desk = GetDC(0)

w = GetSystemMetrics(0)
h = GetSystemMetrics(1)
a = GetSystemMetrics(SM_CXSCREEN)
b = GetSystemMetrics(SM_CYSCREEN)
sw = GetSystemMetrics(0)
sh = GetSystemMetrics(1)
x = GetSystemMetrics(0)
y = GetSystemMetrics(1)
xs = GetSystemMetrics(SM_CXSCREEN)
ys = GetSystemMetrics(SM_CYSCREEN)
i = 0
i < 1900

while True:

    for i in range(0,20):
        BitBlt(desk,10,10,w,h,desk,12,12,SRCAND)
        Sleep(300)
