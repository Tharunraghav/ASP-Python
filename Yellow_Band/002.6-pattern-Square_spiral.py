from turtle import *
import time

color=["darkgoldenrod","goldenrod",'orange','gold','khaki','beige','ivory']
colorv2=["firebrick", "brown", "red", "indianred", "lightcoral", "salmon", "mistyrose"]
colorv3 = ["navy", "steelblue", "deepskyblue", "lightskyblue", "powderblue", "paleturquoise"]
bgcolor('white')
speed(0)
hideturtle()
time.sleep(2)

for i in range(120):
    for j in range(12):
        pencolor(colorv3[i%6])
        fd(.2+i*j)
        left(91)
    penup()
    goto(0,0)
    forward(120)
    right(4)
    pendown()
exitonclick()