import turtle

def star(s, m):
    turtle.left(60)
    for num in range(0, 5):
        turtle.forward(s * m)
        turtle.right(60)
        turtle.forward(s *  m)
        turtle.left(132)
