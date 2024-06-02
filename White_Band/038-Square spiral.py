import turtle
t=turtle.Turtle()
t.speed(2)
length=5
angle=90
while length < 200:
    for i in range (4):
        t.forward(length)
        t.right(angle)
    length+=10
turtle.done(

)