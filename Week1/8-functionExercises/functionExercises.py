# 1 Hello
# Write a function hello which takes a name parameter and says Hello to the name.

# def hello():
#     print('Hello Igor')
#
# hello()

# ##############################################################################
# 2 y = x + 1
# Write a function f(x) that returns x + 1 and plot it for x values of -3 to 3 in increments of 1

# import matplotlib.pyplot as plot
#
# def f(x):
#     # put your code here
#     return x + 1
#
# xs = list(range(-3, 4))
# ys = []
# for x in xs:
#     ys.append(f(x))
#
# plot.plot(xs, ys)
# plot.show()

# ##############################################################################
# 3 Square of x
# Write a function f(x) that returns that square of x

# import matplotlib.pyplot as plot
#
# def squareX(x):
#     return x * x
#
# xValues = []
# for x in range(-100, 100):
#     xValues.append(squareX(x))
#
# plot.plot(xValues)
# plot.show()

# ##############################################################################
# 4 Odd or Even
# Write a function f(x) that returns 1 if x is odd and -1 if x is even.
# Plot it for x values of -5 to 5 in increments of 1. This time, instead of
# using plot.plot, use plot.bar instead to make a bar graph.

# import numpy as np
# import matplotlib.pyplot as plot
#
# def oddOrEven(num):
#     if num % 2 == 0:
#         return -1
#     else:
#         return 1
#
# yValues = []
# for y in range(-5, 6):
#     yValues.append(oddOrEven(y))
#
# ind = np.arange(-5, 6, 1)
# plot.bar(ind, yValues)
# plot.show()

# ##############################################################################
# 5 Sine
# Write a function f(x) that returns the sin of x

# import math
# import matplotlib.pyplot as plot
#
# def sine(y):
#     return math.sin(y)
#
# xValues = []
# yValues = []
#
# for num in range(-5, 6):
#     yValues.append(sine(num))
#     xValues.append(num)
#
# plot.plot(xValues, yValues)
# plot.show()

# ##############################################################################
# 6 Sine 2
# Now plot the graph from -5 to -5 in 0.1 increments

import math
import numpy as np
import matplotlib.pyplot as plot

y = np.arange(-5, 6, 0.1)
xValues = np.arange(-5, 6, 0.1)
yValues = []

def sine(y):
    return math.sin(y)

for num in y:
    yValues.append(sine(num))

plot.plot(xValues, yValues)
plot.show()

# ##############################################################################
# 7 Degree Conversion
# Write a function that takes a temperature in Celcius and converts it Fahrenheit. Plot it on a graph.

# import matplotlib.pyplot as plot
#
# yValues = []
# xValues = []
# while True:
#     def tempC(f):
#         c = (f - 32) * (5/9)
#         yValues.append(c)
#         xValues.append(f)
#     tempF = int(input('Temperature in Fahrenheit? '))
#     if tempF:
#         tempC(tempF)
#         response = input('Would you like to continue? [y][n] ').lower()
#         if response == 'n':
#             break
#     else:
#         print('Please input valid value')
#
# plot.plot(xValues, yValues, 'ro')
# plot.ylabel('Celsius')
# plot.xlabel('Fahrenheit')
# plot.show()

# ##############################################################################
# 8 & 9 Play again? & Play again? Again.
# Write a function that prompts the user for input, asking them
# "Do you want to play again (Y on N)?". If the user answers "Y",
# the function should return True, otherwise, it should return False.
# Write a function that asks the user whether they want to play again last the
# previous problem. Except this time, they have to answer with either "Y" or "N",
# if they give an invalid input, it should say "Invalid input." and prompt the
# user again for an answer. When the user finally gives a valid input, the
# function will return True if it was "Y", and False if it was "N".

# def playAgain(response):
#     if response == 'y':
#         return True
#     elif response == 'n':
#         return False
#     else:
#         response = input('Do you want to play again? (Y or N) ')
#         return playAgain(response)
#
# response = input('Do you want to play again? (Y or N) ')
# print(playAgain(response))
