import win32api
import win32gui
import random
import win32con
from win32gui import *
from win32gui import GetDesktopWindow,GetWindowDC,StretchBlt,BitBlt
from win32api import GetSystemMetrics
from math import *
hwnd = GetDesktopWindow()
hdc2 = GetWindowDC(hwnd)
x = GetSystemMetrics(0)
y = GetSystemMetrics(1)
x2 = GetSystemMetrics(0)
y2 = GetSystemMetrics(1)

import math
import time
desktop = GetDesktopWindow()
left, top, right, bottom = GetWindowRect(desktop)

def redraw():
    RedrawWindow(0, None, None, win32con.RDW_ERASE | win32con.RDW_INVALIDATE |win32con.RDW_ALLCHILDREN );


def radial_move():
 

    while True:
        hdc=GetDC(0)
        memdc = CreateCompatibleDC(hdc)
        hbit = CreateCompatibleBitmap(hdc,x,y)
        sel = SelectObject(memdc,hbit)     
        
        val=random.randint(1,2)
        rateofturning=30
        print(val)
        if val == 1:
            
            PlgBlt(memdc, ((left-rateofturning,top+rateofturning),(right-rateofturning,top-rateofturning),(left+rateofturning,bottom+rateofturning)), hdc, 0, 0, x2, y2, 0, 0, 0);
           
    
 

    
        if val == 2:
            
            PlgBlt(memdc, ((left+rateofturning,top-rateofturning),(right+rateofturning,top+rateofturning),(left-rateofturning,bottom-rateofturning)), hdc, 0, 0, x2, y2, 0, 0, 0);
        
    
        AlphaBlend(hdc,random.randint(-10,10),random.randint(-10,10),x,y,memdc,0,0,x,y, (0,0,70,0))
            
        SelectObject(memdc,sel)
        DeleteObject(sel)
        DeleteObject(hbit)
        DeleteDC(memdc)
        DeleteDC(hdc)
    
def sliding():
    while True:
        
        
        hdc=GetDC(0)
        r=random.randint(0,1)
        if r==1:
            for i in range(10):
                StretchBlt(hdc,0,-50,x,y,hdc,0, 0, x,y, win32con.SRCCOPY);
                StretchBlt(hdc,0,y - 50,x,y,hdc,0, 0, x,y, win32con.SRCCOPY);
        else:
            for i in range(10):
                StretchBlt(hdc,0,50,x,y,hdc,0, 0, x,y, win32con.SRCCOPY);
                StretchBlt(hdc,0,-y + 50,x,y,hdc,0, 0, x,y, win32con.SRCCOPY);

        
sliding()

    

def blurring():
    while True:
    
        hdc=GetDC(0)
        memdc = CreateCompatibleDC(hdc)
        hbit = CreateCompatibleBitmap(hdc,x,y)
        sel = SelectObject(memdc,hbit)
        BitBlt(memdc,0,0,x,y,hdc,0,0,win32con.SRCCOPY)
 
    
        AlphaBlend(hdc,random.randint(-10,10),random.randint(-10,10),x,y,memdc,0,0,x,y, (0,0,70,0))
        
        SelectObject(memdc,sel)
        DeleteObject(sel)
        DeleteObject(hbit)
        DeleteDC(memdc)
        DeleteDC(hdc)
    
        time.sleep(0.2)
def zoom_vertical():
    

    hdc=GetDC(0)
    

        
    for i in range(15):
            
        SetStretchBltMode(hdc, 4)
        StretchBlt (hdc,0,0-10,x2,y2+20,hdc,0,0,x2,y2, win32con.SRCCOPY)
                
        time.sleep(0.2)
                
def zoom_horizontal():
    hdc=GetDC(0)
    for i in range(15):
        SetStretchBltMode(hdc, 4)
        StretchBlt (hdc,0-10,0,x2+20,y2,hdc,0,0,x2,y2, win32con.SRCCOPY)
        time.sleep(0.2)
