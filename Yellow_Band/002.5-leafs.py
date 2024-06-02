from turtle import *
step=6
speed(0)
for i in range(180):
    for j in range(16):
        forward(0.5*i+j)
        left(77/step)
        hideturtle()
        color("black")
        pensize(2)
    left(77)