import turtle
turtle.showturtle()
turtle.shape("turtle")

length=10
angle=90
for i in range(40):
    turtle.forward(length+length)
    turtle.right(angle)
    length=length+10
turtle.done()