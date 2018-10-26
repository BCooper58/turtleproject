from turtle import *
import turtle
color('blue' , 'red')
begin_fill()
while True:
    right(200)
    forward(170)
    if abs(pos()) < 1:
        break
end_fill()
exitonclick()
