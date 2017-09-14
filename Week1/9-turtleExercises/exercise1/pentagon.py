import turtle

def pentagon():
    turtle.Screen()
    turtle.color('pink')
    turtle.shape('turtle')

    for num in range(0, 5):
        turtle.forward(100)
        turtle.left(72)

    turtle.exitonclick()

pentagon()
