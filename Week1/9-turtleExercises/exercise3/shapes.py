import turtle

def circle(s, m):
    turtle.circle(100 * m)

def triangle(s, m):
    for num in range(0, 3):
        turtle.forward(s * m)
        turtle.left(120)

def hexagon(s, m):
    for num in range(0, 6):
        turtle.forward(s * m)
        turtle.left(60)

def octagon(s, m):
    for num in range(0, 8):
        turtle.forward(s * m)
        turtle.left(45)

def pentagon(s, m):
    for num in range(0, 5):
        turtle.forward(s * m)
        turtle.left(72)

def square(s, m):
    for num in range(0, 4):
        turtle.forward(s * m)
        turtle.left(90)

def star(s, m):
    turtle.left(60)
    for num in range(0, 5):
        turtle.forward(s * m)
        turtle.right(60)
        turtle.forward(s *  m)
        turtle.left(132)
