import shapes
import turtle
import random

# funcShapes = [ shapes.circle,
#                 shapes.triangle,
#                 shapes.hexagon,
#                 shapes.octagon,
#                 shapes.pentagon,
#                 shapes.square,
#                 shapes.star ]

def randCol():
    t = ()
    for x in range(3):
        t += (random.randint(0, 255), )
    return t

def pos():
    return random.randint(-175, 175)

def runShapes():
    for x in range(0, 50):
        sh = random.randint(0, 360)
        # spd = random.randint(0, 11)
        p = random.randint(0, 20)
        multi = random.randint(1, 3)
        size = random.randint(20, 50)
        turtle.Screen()
        turtle.begin_fill()
        turtle.shape('turtle')
        turtle.colormode(255)
        turtle.bgcolor(randCol())
        turtle.color(randCol(), randCol())
        turtle.pensize(p)
        turtle.speed(10)
        turtle.seth(sh)
        turtle.penup()
        turtle.goto(pos(), pos())
        turtle.pendown()
        shapes.star(size, multi)
        turtle.end_fill()
    turtle.exitonclick()

if __name__ == '__main__':
    runShapes()
