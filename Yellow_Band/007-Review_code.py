import turtle
t=turtle.Turtle()
def drawShape(color, shape, length, angle):
    t.begin_fill()
    t.fillcolor(color)
    for i in range(shape):
        t.forward(length)
        t.left(angle)
    t.end_fill()
def jumpTo(x, y):
    t.penup()
    t.goto(x,y)
    t.pendown()

drawShape("red", 8, 50, 45)
jumpTo(-142,25)
drawShape("green", 6, 50, 60)
jumpTo(142,25)
drawShape("blue", 7, 50, 52)
jumpTo(142,-155)
drawShape("yellow", 11, 50, 32)
jumpTo(-142,-155)
drawShape("purple", 10, 50, 37)
jumpTo(0,-250)
drawShape("pink", 9, 50, 41)