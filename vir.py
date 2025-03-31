from win32con import * # win32con import.
from win32file import * # win32file import.
from win32gui import * # win32gui import.
from win32api import * # win32api import.
from win32ui import * # win32ui import.
from random import * # random import.
from tkinter import * # tkinter import.
from ctypes import windll # ctypes import.
from random import randrange as rd # random, randrange etc. settings vb. import.
import multiprocessing # multiprocessing import.
import rotatescreen #rotatescreen import.
import win32gui as wgui # wgui import name.
import tkinter as tk # tkinter settings cache vb. etc. import.
import commctrl as cc # commctrl import.
import time # time import.
import subprocess # subprocess import.
import pyautogui # pyautogui import.
import webbrowser # importing webbrowser.
import time #time import for tunnel effects etc.
import random # random prompt cache etc. import.
import ctypes # ctypes settings cache. etc. vb. import.
import sys # system import.
import os #os import.
import winsound # winsound import for bytebeat.              

PhotoImg = r'C:\Windows\Web\Screen\img105.jpg'
ctypes.windll.user32.SystemParametersInfoW(20, 0, PhotoImg, 0)


desk = GetDC(0)

x = GetSystemMetrics(0)
y = GetSystemMetrics(1)

for i in range(0, 100):
    PatBlt(desk, 0, 0, x, y, PATINVERT)


desk = GetDC(0)
x = GetSystemMetrics(0)
y = GetSystemMetrics(1)


for i in range(0, 100):
    brush = CreateSolidBrush(RGB(
        randrange(225),
        randrange(225),
        randrange(225),
        ))
    SelectObject(desk, brush)
    PatBlt(desk, randrange(x), randrange(y), randrange(x), randrange(y), PATINVERT)
    DeleteObject(brush)
    Sleep(10)



screen = rotatescreen.get_primary_display()
for i in range(13):
    time.sleep(1)
    screen.rotate_to(i*90 % 360)

desk = GetDC(0)
x = GetSystemMetrics(0)
y = GetSystemMetrics(1)
w = GetSystemMetrics(0)
h = GetSystemMetrics(1)
sw = GetSystemMetrics(0)
sh = GetSystemMetrics(1)
a = GetSystemMetrics(SM_CXSCREEN)
b = GetSystemMetrics(SM_CYSCREEN)
 
for i in range(0, 1000):
	brush = CreateSolidBrush(RGB(
		0,
		255,
		0,
                ))
	PatBlt(desk, 0, 0, x, y, PATINVERT)
	PatBlt(desk,randrange(x),randrange(y),randrange(x),randrange(y),PATINVERT)
	BitBlt(desk,10,10,w,h,desk,12,12,SRCAND)
	StretchBlt(desk, -20, -20, sw+40, sh+40, desk, 0, 0, sw, sh, 0x9999999)
 
	StretchBlt(GetDC(NULL), 50, 50, a - 100, b - 100, GetDC(NULL), 0, 0, a, b, SRCINVERT)
	DeleteObject(brush)
	Sleep(10)
