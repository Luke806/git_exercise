import turtle

def print_goto(p_x,p_y):
    turtle.penup()
    turtle.goto(p_x,p_y)
    turtle.pendown()


def print_square():
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
def print_triangle():
    for i in range(3):
        turtle.forward(100)
        turtle.left(120)

x_location = -300
for i in range(5):
    print_goto(x_location,0)
    print_square()
    x_location += 120
