from gturtle import *
from time import sleep

SCREEN_LEFT = -400
SCREEN_RIGHT = -SCREEN_LEFT
SCREEN_TOP = 300
SCREEN_BOTTOM = -SCREEN_TOP



KEYSPEED = 6
MAXSPEED = 12
JUMPSPEED = 10
JUMPFACTOR = 2
GRAVITY = 1
DAMPING = 0.75
JUMPDAMING = 0.95
LOOPDELAY = 0.1	

LEFT = -1
RIGHT = -1
GROUNDLEVEL = SCREEN_BOTTOM + 36

BREAK = False
CHARACTER_HEIGHT = 7
CHARACTER_WIDTH = 8

pos_x = SCREEN_LEFT +10
pos_y = GROUNDLEVEL
speed_x = 0
speed_y = 0
direction = 0

def bound(x, min_x, max_x):
	return min(max(x, min_x), max_x)
	
def update():

