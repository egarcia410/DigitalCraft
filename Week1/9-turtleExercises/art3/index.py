import turtle

xShift = -187.5
yShift = 25

def trapezoid():
    startPoint = [[0, 0], [270, 0], [105, 50], [375, 50]]
    sides = [105, 60, 45, 60]
    angles = [0, 240, 180, 120]
    colors = ['#288ECA', '#F79E34', '#7EC04B', '#BBBDBF']

    for index, point in enumerate(startPoint):
        turtle.penup()
        # Add shift variables to point
        turtle.goto(point[0], point[1])
        if index == 2:
            sides = sides[::-1]
            angles = angles[::-1]
        turtle.begin_fill()
        for index1, side in enumerate(sides):
            turtle.pendown()
            turtle.color(colors[index])
            turtle.seth(angles[index1])
            turtle.forward(side)
        turtle.end_fill()

def rhombus(startPoint, colors, sides):
    angles = [0, 240, 180, 60]
    for index, point in enumerate(startPoint):
        turtle.penup()
        # Add shift variables to point
        turtle.goto(point[0], point[1])
        print(turtle.position())
        if index == 2:
            angles[1] = 120
            angles[3] = 300
        turtle.begin_fill()
        for index1, side in enumerate(sides):
            turtle.pendown()
            turtle.color(colors[index])
            turtle.seth(angles[index1])
            print(angles[index1], 'heading angle')
            print(side, 'side length')
            print('--------------------')
            turtle.forward(side)
        turtle.end_fill()

# def triangle():





if __name__ == '__main__':
    bPoints = [[105, 0], [255, 101.96], [105, 50], [255, -51.96]]
    bColors = ['#1771B5', '#A6AAAB', '#5D8842', '#F27830']
    bSides = [45, 60, 45, 60]
    sPoints = [[119.5, 24.88], [225, 50], [119.5, 24.85], [225, 0]]
    sColors = ['#2A94CE', '#BBBDBF', '#8FC449', '#FBB231']
    sSides = [45, 29, 45, 29]
    trapezoid()
    rhombus(bPoints, bColors, bSides)
    rhombus(sPoints, sColors, sSides)
    turtle.exitonclick()
