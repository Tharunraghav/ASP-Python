import turtle
shape=input("what shape do you want to draw(Square,circle,triangle):")
shape.lower()
if shape=="square":
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.fillcolor("orange("orange")

    turtle.done()

elif shape=='circle':
    turtle.circle(50)
    turtle.done()
elif shape=='triangle':
    for i in range(3):
        turtle.forward(100)
        turtle.left(120)
        turtle.done()
else:
    print("Please enter only the above given shapes")