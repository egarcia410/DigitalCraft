import turtle

def octagon():
    turtle.Screen()
    turtle.color('purple')
    turtle.shape('turtle')

    for num in range(0, 8):
        turtle.forward(100)
        turtle.left(45)

    turtle.exitonclick()

octagon()
