from gturtle import *
from time import sleep
import numpy as np

SCREEN_LEFT = -400
SCREEN_RIGHT = -SCREEN_LEFT
SCREEN_TOP = 300
SCREEN_BOTTOM = -SCREEN_TOP

PLATFORMS = [(np.random.randint(-301,301,1), np.random.randint(-301,301,1), np.random.randint(-401,401,1)),
             (np.random.randint(-301,301,1), np.random.randint(-301,301,1), np.random.randint(-401,401,1)),
             (np.random.randint(-301,301,1), np.random.randint(-301,301,1), np.random.randint(-401,401,1)),
             (np.random.randint(-301,301,1), np.random.randint(-301,301,1), np.random.randint(-401,401,1)),
             (np.random.randint(-301,301,1), np.random.randint(-301,301,1), np.random.randint(-401,401,1)),
             (np.random.randint(-301,301,1), np.random.randint(-301,301,1), np.random.randint(-401,401,1)),
             (np.random.randint(-301,301,1), np.random.randint(-301,301,1), np.random.randint(-401,401,1)),
             (np.random.randint(-301,301,1), np.random.randint(-301,301,1), np.random.randint(-401,401,1)),
             (np.random.randint(-301,301,1), np.random.randint(-301,301,1), np.random.randint(-401,401,1)),
             (np.random.randint(-301,301,1), np.random.randint(-301,301,1), np.random.randint(-401,401,1)),
             (np.random.randint(-301,301,1), np.random.randint(-301,301,1), np.random.randint(-401,401,1)),
             (np.random.randint(-301,301,1), np.random.randint(-301,301,1), np.random.randint(-401,401,1))]
             
GOAL = (np.random.randint(-301,301,1))

KEYSPEED = 6
MAXSPEED = 12
JUMPSPEED = 10
JUMPFACTOR = 2
GRAVITY = 1
DAMPING = 0.75
JUMPDAMPING = 0.95
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
	global pos_x, pos_y, speed_x, speed_y
	gl = getGroundLevel(pos_x, pos_y)
	if gl < pos_y or speed_y > 0:
		speed_y = bound(speed_y + GRAVITY, -MAXSPEED, MAXSPEED)
	else:
		speed_y == 0
		
	if speed_x !=0:
		if speed_y == 0:
			speed_x = bound(speed_x * DAMPING, -MAXSPEED, MAXSPEED)
		else:
			speed_x = bound(speed_x * JUMPDAMPING, -MAXSPEED, MAXSPEED)
		if -0.5 < speed_x < 0.5:
			speed_x = 0
			
		if speed_x != 0 or speed_y !=0:
			pos_x = bound(pos_x + speed_x, SCREEN_LEFT, SCREEN_RIGHT)
			pos_y = bound(pos_y + speed_y, gl, SCREEN_TOP)
			setPos(pos_x, pos_y + CHARACTER_HEIGHT)
			
def setSpeed(speedX=none, speedY=none):
	global speed_x, speed_y, direction
	if speedX != None:
		speed_x = speedX
	if speedY != None:
		speed_y = speedY
	if speed_x >= 0:
		d = RIGHT
	else:
		d = LEFT
		
def getGroundLevel(x, y):
	result = GROUNDLEVEL
	cw = CHARACTER_WIDTH // 2
	for x_left, x_right, height in PLATFORMS:
		if x_left-cw <= x <= x_right+cw:
			gl = GROUNDLEVEL + height
			if y >= gl and gl > result:
				result = gl
	return result
	
def goalReached():
	goal_x, goal_y, radius = GOAL
	delta_x = (pos_x - goal_x) ** 2
	delta_y = (pos_y - (goal_y+GROUNDLEVEL)) ** 2
	return ((delta_x + delta_y) <= (radius ** 2))

def paintPlatforms():
    penWidth(8)
    setPenColor(makeColor("sky blue"))
    for x_left, x_right, height in PLATFORMS:
        y = GROUNDLEVEL + height - 5
        setPos(x_left, y)
        moveTo(x_right, y)
	
def paintGoal():
	goal_x, goal_y, radius = GOAL
	setPenColor(makeColor("gold"))
	setPos(goal_x, goal_y + GROUNDLEVEL)
	dot(radius)
	setPenColor("black")
	dot(radius * 3 // 4)
	
def paintScene():
    clear(makeColor("#006eff"))
    setPenColor(makeColor("#49321f"))
    fillRectangle(SCREEN_LEFT, GROUNDLEVEL, SCREEN_RIGHT, SCREEN_BOTTOM)
    paintPlatforms()
    paintGoal()
    penUp()
	
def onKeyPressed(code):
	global speed_x, speed_y, BREAK
	if code == 37:
		if speed_y == 0:
			speed_x += LEFT * KEYSPEED
	elif code == 38:
		if speed_y == 0:
			speed_y = max(JUMPSPEED, JUMPFACTOR * abs(speed_x))
	elif code == 39:
		if speed_y == 0:
			speed_x += RIGHT * KEYSPEED
	elif code == 27:
		BREAK = True
		
makeTurtle("sprite.png", keyPressed=onKeyPressed)
hideTurtle()
paintScene()
moveTo(pos_x, pos_y + CHARACTER_HEIGHT)
setSpeed(None, None)
showTurtle()
heading(0)

repeat:
	sleep(LOOPDELAY)
	if BREAK or isDisposed():
		break
	update()
	if goalReached():
		msgDlg("Great Job!")
		break
		
dispose()
			
	

