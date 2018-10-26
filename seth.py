from turtle import *
import turtle
speed(1)
def Seth():
    color('orange' , 'black')
    begin_fill()
    while True:
        right(250)
        forward(270)
        left(200)
        forward(100)
        if abs(pos()) < 3:
            break
    end_fill()
    exitonclick()
Seth()
