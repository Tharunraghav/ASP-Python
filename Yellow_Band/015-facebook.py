import turtle
t=turtle.Turtle()

#background

#bg color
t.penup()
t.backward(100)
t.pendown()
t.color('blue','blue')
t.begin_fill()
for i in range(4):
    t.forward(200)
    t.left(90)
t.end_fill()

#drawing f
t.penup()
t.forward(100)
t.left(90)
t.forward(10)
t.pensize(20)
t.color('white')
t.pendown()

t.forward(80)
t.left(90)
t.forward(30)
t.backward(60)
t.forward(30)
t.right(90)
t.forward(40)
for i in range(30):
    t.forward(1)
    t.right(3)
t.forward(15)



turtle.done()