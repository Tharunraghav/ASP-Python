from turtle import *

for i in range(50):
    for j in range(4):
        forward(0.2*i*j)
        left(91)
        hideturtle()
        pensize(3)
        speed(50)
    left(73*15/100+10)
