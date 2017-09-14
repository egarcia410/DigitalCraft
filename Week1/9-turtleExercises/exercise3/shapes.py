import turtle

def circle():
    turtle.circle(100)

def triangle():
    for num in range(0, 2):
        turtle.forward(100)
        turtle.left(120)
    turtle.forward(100)

def hexagon():
    for num in range(0, 6):
        turtle.forward(100)
        turtle.left(60)

def octagon():
    for num in range(0, 8):
        turtle.forward(100)
        turtle.left(45)

def pentagon():
    for num in range(0, 5):
        turtle.forward(100)
        turtle.left(72)

def square():
    for num in range(0, 4):
        turtle.forward(100)
        turtle.left(90)

def star():
    turtle.left(60)
    for num in range(0, 5):
        turtle.forward(100)
        turtle.right(60)
        turtle.forward(100)
        turtle.left(132)
