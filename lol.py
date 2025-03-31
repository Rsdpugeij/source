import sys
from win32con import *
from win32gui import *
from win32api import *
from random import *
dc = GetDC(0)
def draw_rects(dc, x, y, w, h, count, dx, dy):
    for i in range(count):
        brush = CreateSolidBrush(RGB(randrange(255),randrange(255),randrange(255)))
        SelectObject(dc, brush)
        #PatBlt(dc, x + i * dx, y + i * dy, w - 2 * i * dx, h - 2 * i * dy, BLACKNESS)
        PatBlt(dc, x + i * dx, y + i * dy, w - 2 * i * dx, h - 2 * i * dy, PATINVERT)
while True:
    draw_rects(dc, randrange(0,1920), randrange(0,1079), 250, 250, 120, 10, 10)