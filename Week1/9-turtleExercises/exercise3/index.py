import shapes
import turtle
import random

funcShapes = [ shapes.circle,
                shapes.triangle,
                shapes.hexagon,
                shapes.octagon,
                shapes.pentagon,
                shapes.square,
                shapes.star ]

def randCol():
    t = ()
    for x in range(3):
        t += (random.randint(0, 255), )
    return t

def pos():
    return random.randint(-150, 150)

def runShapes():
    for func in funcShapes:
        sh = random.randint(0, 360)
        spd = random.randint(0, 11)
        p = random.randint(0, 20)
        multi = random.randint(1, 3)
        size = random.randint(20, 50)
        turtle.Screen()
        turtle.bgcolor('blue')
        turtle.begin_fill()
        turtle.shape('turtle')
        turtle.colormode(255)
        turtle.color(randCol(), randCol())
        turtle.pensize(p)
        turtle.speed(spd)
        turtle.seth(sh)
        turtle.penup()
        turtle.goto(pos(), pos())
        turtle.pendown()
        func(size, multi)
        turtle.end_fill()
    turtle.exitonclick()

if __name__ == '__main__':
    runShapes()
