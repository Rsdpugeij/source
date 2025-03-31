from pynput.mouse import Button, Controller
import random as ran
import math
my_mouse = Controller()
offsetmax = 100
while True:
    offsetmin = offsetmax
    x,y = my_mouse.position
    offsetx = ran.randint(offsetmin,offsetmax)
    offsety = ran.randint(offsetmin,offsetmax)
    yeql = math.fmod(y + offsety,1079)
    xeql = math.fmod(x + offsetx,1919)
    my_mouse.position = (xeql,yeql)
    my_mouse.click(Button.left, 1)
    my_mouse.click(Button.right, 1)

