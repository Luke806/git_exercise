print('hello lucas~')
import turtle
def print_goto(p_x,p_y):
    turtle.penup()
    turtle.goto(p_x,p_y)
    turtle.pendown()


def print_square():
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)
print_square()
print_goto(120,0)
def print_triangle():
    for i in range(3):
        turtle.forward(100)
        turtle.left(120)
print_triangle()
