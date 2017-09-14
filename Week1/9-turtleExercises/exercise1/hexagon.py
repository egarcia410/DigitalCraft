import turtle

def hexagon():
    turtle.Screen()
    turtle.color('yellow')
    turtle.shape('turtle')

    for num in range(0, 6):
        turtle.forward(100)
        turtle.left(60)

    turtle.exitonclick()

hexagon()
