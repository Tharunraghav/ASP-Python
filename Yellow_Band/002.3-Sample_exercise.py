from turtle import*

for i in range(420):
    for j in range(4):
        forward(2 * i * j)
        left(65)
        hideturtle()
        pensize(1)
        speed(0)
penup()
goto(0,0)
left(33*2.5)
pendown()