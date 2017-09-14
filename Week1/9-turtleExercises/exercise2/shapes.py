import turtle
turtle.Screen()

print(__name__, 'name')

def circle():
    turtle.color('green')
    turtle.shape('turtle')
    turtle.circle(100)

def triangle():
    turtle.color('blue')
    turtle.shape('turtle')
    for num in range(0, 2):
        turtle.forward(100)
        turtle.left(120)
    turtle.forward(100)

def hexagon():
    turtle.color('yellow')
    turtle.shape('turtle')
    for num in range(0, 6):
        turtle.forward(100)
        turtle.left(60)

def octagon():
    turtle.color('purple')
    turtle.shape('turtle')
    for num in range(0, 8):
        turtle.forward(100)
        turtle.left(45)

def pentagon():
    turtle.color('pink')
    turtle.shape('turtle')
    for num in range(0, 5):
        turtle.forward(100)
        turtle.left(72)

def square():
    turtle.color('black')
    turtle.shape('turtle')
    for num in range(0, 4):
        turtle.forward(100)
        turtle.left(90)

def star():
    turtle.color('red')
    turtle.shape('turtle')
    turtle.left(60)
    for num in range(0, 5):
        turtle.forward(100)
        turtle.right(60)
        turtle.forward(100)
        turtle.left(132)
