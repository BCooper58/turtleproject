import turtle
from time import sleep

def paintScene():
    clear(makeColor("#006eff"))
    setPenColor(makeColor("#49321f"))
    fillRectangle(SCREEN_LEFT, GROUNDLEVEL, SCREEN_RIGHT, SCREEN_BOTTOM)
    paintPlatforms()
    paintGoal()
    penUp()
