# 1 1 to 10
# Using a for loop and the range function, print out the numbers
# between 1 and 10 inclusive, one on a line.

# for num in range(0, 11):
#     print(num)

################################################################################
# 2 n to m
# Same as the previous problem, except you will prompt the user for the
# number to start on and the number to end on.

# start = int(input('Start from: '))
# end = int(input('End on: '))
#
# if end < start:
#     for num in range(start, end-1, -1):
#         print(num)
#
# for num in range(start, end+1):
#     print(num)

################################################################################
# 3 Odd Numbers
# Print each odd number between 1 and 10 inclusive.

# for num in range(1, 10, 2):
#     print(num)

################################################################################
# 4 Print a Square
# Print a 5x5 square of * characters

# for x in range(5):
#     print('*' * 5)

################################################################################
# 5 Print a Square
# Print a NxN square of * characters. Prompt the user for N.

# size = int(input('How big is the square? '))
#
# for x in range(size+1):
#         print('*' * size)

################################################################################
# 6 Print a Box
# Given a height and width, input by the user, print a box
# consisting of * characters as its border.

# width = int(input('Width? '))
# height = int(input('Height? '))
#
# for x in range(height):
#     if x == 0 or x == height - 1:
#         print('*' * width)
#     else:
#         print('*' + (' ' * (width - 2)) + '*')

################################################################################
# 7 Print a Triangle
# Print a triangle consisting of * characters

# sideBuffer = 3
# star = 1
# while sideBuffer != -1:
#     print((' ' * sideBuffer) + ('*' * star) + (' ' * sideBuffer))
#     sideBuffer -= 1
#     star += 2

################################################################################
# 8  Print a Triangle II
# Given a number as the height, print a triangle as in "Print a Triangle" but with the given height.

# sideBuffer= int(input('How tall is the triangle? '))
# star = 1
#
# while sideBuffer != 0:
#     print((' ' * sideBuffer) + ('*' * star) + (' ' * sideBuffer))
#     sideBuffer -= 1
#     star += 2

################################################################################
# 9 Multiplication Table
# Print the multiplication table for numbers from 1 up to 10

# firstDigit = 1
# while firstDigit != 11:
#     secondDigit = 1
#     while secondDigit != 11:
#         first = str(firstDigit)
#         second = str(secondDigit)
#         total = str(firstDigit * secondDigit)
#         print(first + ' X ' + second + ' = ' + total)
#         secondDigit += 1
#     firstDigit += 1

################################################################################
# Bonus: Print a Banner
# Given a string, input by the user, print that string with a box around it.
# The box should stretch to the length of the string.

# text = input('Text? ')
#
# print(('*' * (len(text)+4)))
# print('* ' + text + ' *')
# print(('*' * (len(text)+4)))

################################################################################
# Bonus: Triangle Numbers

# for x in range(101):
#     print(x, x * (x+1) / 2)

################################################################################
# Bonus: Factor a Number
# Given a number, print its factors.

numInput = int(input('Pick a number! '))

factors = []

for num in range(1, numInput + 1):
    if numInput % num == 0:
        factors.append(num)

print(factors)
