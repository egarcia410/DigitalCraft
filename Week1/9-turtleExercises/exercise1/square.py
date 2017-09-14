import turtle

def square():
    turtle.Screen()
    turtle.color('black')
    turtle.shape('turtle')
    for num in range(0, 4):
        turtle.forward(100)
        turtle.left(90)
    turtle.exitonclick()

square()
