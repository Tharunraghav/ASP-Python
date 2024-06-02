import turtle
smile_type=input("What type of smiley you want to draw(sad , happy,surprised):")
t=turtle.Turtle()

if smile_type=='happy':
    t.circle(50)
    t.penup()
    t.goto(-15,60)
    t.pendown()
    t.circle(5)
    t.penup()
    t.goto(15,60)
    t.pendown()
    t.circle(5)
    t.penup()
    t.goto(-25,40)
    t.pendown()
    t.seth(-75)
    t.circle(25,180)

elif smile_type=="surprised":
    t.circle(50)
    t.penup()
    t.goto(-15,60)
    t.pendown()
    t.circle(5)
    t.penup()
    t.goto(15,60)
    t.pendown()
    t.circle(5)
    t.penup()
    t.goto(0,5)
    t.pendown()
    t.circle(20)

elif smile_type=="sad":
    t.circle(50)
    t.penup()
    t.goto(-15,60)
    t.pendown()
    t.circle(5)
    t.penup()
    t.goto(15,60)
    t.pendown()
    t.circle(5)
    t.penup()
    t.goto(-15,5)
    t.pendown()
    t.seth(-75)
    t.circle(20,-180)



