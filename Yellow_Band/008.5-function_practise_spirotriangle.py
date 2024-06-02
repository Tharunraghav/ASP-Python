import turtle
def draw_triangle(side_length):
    for _ in range(3):
        turtle.forward(side_length)
        turtle.right(120)

def draw_spiro_triangle(side_length, depth):
    angle = 360/depth
    for _ in range(depth):
        draw_triangle(side_length)
        turtle.right(angle)


turtle.speed(0)


draw_spiro_triangle(100, 10)

turtle.done()