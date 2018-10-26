
from turtle import *
from random import randint

bgcolor('black')
x = 1
speed(0)
while x < -500:

	r = randint(0,255)
	g = randint(0,255)
	b = randint(0,255)

	colormode(255)
	pencolor(r,g,b)
	fd(50 + x)
	rt(90.911)
	x = x-1
	print(x,r,g,b)
exitonclick()
