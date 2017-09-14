import turtle

def star():
    turtle.Screen()
    turtle.color('red')
    turtle.shape('turtle')
    turtle.left(60)

    for num in range(0, 5):
        turtle.forward(100)
        turtle.right(60)
        turtle.forward(100)
        turtle.left(132)
    turtle.exitonclick()

star()
