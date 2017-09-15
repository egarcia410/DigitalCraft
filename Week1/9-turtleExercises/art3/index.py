import turtle

# Centers logo to background
# xShift = -187.5
# yShift = 25
xShift = -200
yShift = 40

def trapezoid():
    startPoint = [[0, 0], [270, 0], [105, 50], [375, 50]]
    sides = [105, 60, 45, 60]
    angles = [0, 240, 180, 120]
    colors = ['#288ECA', '#F79E34', '#7EC04B', '#BBBDBF']

    for index, point in enumerate(startPoint):
        turtle.penup()
        turtle.goto(point[0] + xShift, point[1]+ yShift)
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

def rhombus(points, colors, sides):
    angles = [0, 240, 180, 60]
    for index, point in enumerate(points):
        turtle.penup()
        turtle.goto(point[0] + xShift, point[1] + yShift)
        if index == 2:
            angles[1] = 120
            angles[3] = 300
        turtle.begin_fill()
        for index1, side in enumerate(sides):
            turtle.pendown()
            turtle.color(colors[index])
            turtle.seth(angles[index1])
            turtle.forward(side)
        turtle.end_fill()

def triangle(points, colors, side, angles):
    angles = angles
    for index, point in enumerate(points):
        turtle.penup()
        turtle.goto(point[0] + xShift, point[1] + yShift)
        if index == 3:
            angles = angles[::-1]
        if len(points) < 3 and index == 1:
            angles[0] = 60
            angles[2] = 300
        turtle.begin_fill()
        for ind in range(0, 3):
            turtle.pendown()
            turtle.color(colors[index])
            turtle.seth(angles[ind])
            turtle.forward(side)
        turtle.end_fill()

if __name__ == '__main__':
    # Big Rhombus - points, colors, length sides
    bRPoints = [[105, 0], [255, 101.96], [105, 50], [255, -51.96]]
    bRColors = ['#1771B5', '#A6AAAB', '#5D8842', '#F27830']
    bRSides = [45, 60, 45, 60]
    # Small Rhombus - points, colors, length sides
    sRPoints = [[119.5, 24.88], [225, 50], [119.5, 24.85], [225, 0]]
    sRColors = ['#2A94CE', '#BBBDBF', '#8FC449', '#FBB231']
    sRSides = [45, 29, 45, 29]
    # Big triangle - points, colors, lengths sides, angle
    bTPoints = [[119.5, 24.88], [142.00,63.85], [210.5, 25.12],
                [164.5, 24.88], [255.5, 25.12], [233.00,-13.85]]
    bTColors = ['#1B67A1', '#1F84B1', '#C08258', '#F27830', '#939597', '#6E6E71']
    bTSides = 45
    bTAngles = [0, 240, 120]
    # Small triangle - points, colors, lengths sides, angle
    sTPoints = [[187.00,63.85], [188.00,-13.85]]
    sTColors = ['#1B67A1', '#1F84B1']
    sTSides = 40
    sTAngles = [300, 180, 60]

    trapezoid()
    rhombus(bRPoints, bRColors, bRSides)
    rhombus(sRPoints, sRColors, sRSides)
    triangle(bTPoints, bTColors, bTSides, bTAngles)
    triangle(sTPoints, sTColors, sTSides, sTAngles)
    turtle.hideturtle()
    turtle.exitonclick()
