import turtle

#Drawing Diamond
turtle.color("black","Yellow")
turtle.pensize(3)
turtle.begin_fill()
turtle.speed(5)
turtle.left(50)
turtle.forward(180)
turtle.left(80)
turtle.forward(160)
turtle.left(100)
turtle.forward(150)
turtle.left(70)
turtle.forward(165)
turtle.end_fill()

#Drawing Black bg inside
turtle.penup()
turtle.left(110)
turtle.forward(80)
turtle.pendown()
turtle.left(130)
turtle.begin_fill()
turtle.color("Black")
turtle.forward(85)
turtle.right(90)
turtle.forward(135)
turtle.right(90)
turtle.forward(85)
turtle.right(90)
turtle.forward(135)
turtle.end_fill()

#lights

#red
turtle.fillcolor("red")
turtle.penup()
turtle.right(180)
turtle.forward(120)
turtle.left(90)
turtle.forward(40)
turtle.pendown()
turtle.begin_fill()
turtle.circle(16)
turtle.end_fill()

#yellow
turtle.penup()
turtle.forward(16)
turtle.left(90)
turtle.forward(52)
turtle.pendown()
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(16)
turtle.end_fill()

#green
turtle.penup()
turtle.forward(40)
turtle.fillcolor("green")
turtle.begin_fill()
turtle.circle(15)
turtle.end_fill()
turtle.hideturtle()
turtle.done()