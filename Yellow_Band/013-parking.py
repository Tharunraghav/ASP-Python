import turtle
turtle.speed(1)
turtle.shape("turtle")
#outer blue circle
turtle.fillcolor("deepskyblue")
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

#inner white circle
turtle.left(90)
turtle.penup()
turtle.forward(10)
turtle.pendown()
turtle.right(90)
turtle.pencolor("white")
turtle.pensize(2)
turtle.circle(90)

#P
turtle.penup()
turtle.left(90)
turtle.forward(30)
turtle.left(90)
turtle.forward(20)
turtle.right(90)
turtle.pendown()
#drawing
turtle.pensize(10)
turtle.forward(120)
turtle.right(90)
turtle.forward(20)
for i in range(180):
    turtle.forward(0.5)
    turtle.right(1)
turtle.forward(20)
turtle.hideturtle()
turtle.done()