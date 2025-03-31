from pynput.mouse import Button, Controller
import random as ran
my_mouse = Controller()
offsetmax = 1
offsetmin = 0 - offsetmax
while True:
    x,y = my_mouse.position
    offsetx = ran.randint(offsetmin,offsetmax)
    offsety = ran.randint(offsetmin,offsetmax)
    my_mouse.position = ((x + offsetx),(y + offsety))
    my_mouse.click(Button.left, 1)
