
from turtle import *
from random import randint
t = Turtle()
t.bgcolor('black')
x = 1
t.speed(0)
while x < 500:

	r = randint(0,255)
	g = randint(0,255)
	b = randint(0,255)

	t.colormode(255)
	t.pencolor(r,g,b)
	t.fd(50 + x)
	t.rt(90.911)
	x = x+1

exitonclick()
