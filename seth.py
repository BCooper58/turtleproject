from turtle import *
import turtle
speed(0)
def Seth():
    color('black' , 'green')
    begin_fill()
    while True:
        right(250)
        forward(270)
        if abs(pos()) < 1:
            break
    end_fill()
    exitonclick()
Seth()
