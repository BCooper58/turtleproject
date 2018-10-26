from turtle import *

def box():
	penup()
	setposition(-125, -300)
	color("black")
	pendown()
	forward(250)
	left(90)
	forward(250)
	left(90)
	forward(250)
	left(90)
	forward(250)
	

def lever():
	penup()
	setposition(125, -150)
	pendown()
	circle(10)
	penup()
	setposition(135, -145)
	left(45)
	pendown()
	forward(100)
	
	
def body():
	penup()
	setposition(-35,-35)
	pendown()
	circle(45)
	penup()
	setposition(-35,55)
	pendown()
	circle(45)
	penup()
	setposition(-50,150)
	pendown()
	circle(65)


def face():
	penup()
	setposition(-39, 210)
	pendown()
	circle(8)
	penup()
	setposition(-34, 216)
	color("red")
	pendown()
	dot()
	penup()
	color("black")
	setposition(14, 210)
	pendown()
	circle(8)
	penup()
	setposition(19, 216)
	color("red")
	pendown()
	dot()
	penup()
	color("black")
	setposition(1, 205)
	pendown()
	right(90)
	forward(10)
	right(90)
	forward(10)
	penup()
	color("red")
	setposition(-18, 175)
	pendown()
	right(135)
	forward(27)
	color("black")
	
	
def hat():
	penup()
	setposition(-85, 260)
	pendown()
	forward(160) 
	penup()
	setposition(-39, 260)
	pendown()
	left(90)
	forward(85)
	right(90)
	forward(58)
	right(90)
	forward(85)

	
def BRENDEN():
	box()
	lever()
	body()
	face()
	hat()
	done()
	
	
BRENDEN()

