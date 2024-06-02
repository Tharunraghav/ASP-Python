import turtle
a=int(input("enter length in hundreds:"))
b=int(input("enter breadth in hundreds(less than length value) :" ))
wr=turtle.write("Tharun",align='left',font=('arial',25,'bold'))

turtle.forward(a)
turtle.left(90)
turtle.forward(b)
turtle.left(90)
turtle.forward(a)
turtle.left(90)
turtle.forward(b)
turtle.done()
