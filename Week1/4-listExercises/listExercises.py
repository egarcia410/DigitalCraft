# 1 Sum the Numbers
# Given an list of numbers, print their sum. When I say given something,
# just make something up and store it in a variable.

numbers = [99, 70, -1, 85, 59, 67,	-51, -42, -37, -15]
numbers2 = [36, 24, -89, 63, 45, -12, 8, -77, 33, 4]

# print(sum(numbers))

# #############################################################################
# 2 Largest Number
# Given an list of numbers, print the largest of the numbers.

# print(max(numbers))

###############################################################################
# 3 Smallest Number
# Given an list of numbers, print the smallest of the numbers.

# print(min(numbers))

###############################################################################
# 4 Even Numbers
# Given an list of numbers, print each number in the list that is even.

# for num in numbers:
#     if num % 2 == 0:
#         print(num)

# result = list(filter(lambda x: x % 2 == 0, numbers))
# print(result)

###############################################################################
# 5 Positive Numbers
# Given an list of numbers, print each number in the list that is greater than zero.

# for num in numbers:
#     if num > 0:
#         print(num)

###############################################################################
# 6 Positive Numbers II
# Given an list of numbers, create a new list which contains every number in the given list which is positive.

# result = list(filter(lambda x: x > 0, numbers))
# print(result)

###############################################################################
# 7 Multiply a list
# Given an list of numbers, and a single factor (also a number), create a new
# list consisting of each of the numbers in the first list multiplied by the factor. Print this list.

# single_factor = 3
# def multiplyNum(n):
#     return n * single_factor

# result = list(map(multiplyNum, numbers))
# result = list(map(lambda x: x * single_factor, numbers))
# print(result)

###############################################################################
# 8 Multiply Vectors
# Given two lists of numbers of the same length, create a new list by
# multiplying the pairs of numbers in corresponding positions in the two lists.

# result = list(map(lambda i,j: i*j, numbers, numbers2))
# print(result)
#
# result = []
# for index, num in enumerate(numbers):
#     result.append(num * numbers2[index])
# print(result)

###############################################################################
# 9 & 10 Matrix Addition & Matrix Addition II
# Calculate the result of adding the two matrices.
# Use your solution in Matrix Addition, and extend it to work for a pair
# of matrices of any size, as long as they have the same size.

matrix1 = [ [2, -2],
            [5, 3] ]

matrix2 = [ [3, 1],
            [7, 9] ]

# result = []
# outerIndex = 0
# for item in matrix1:
#     innerIndex = 0
#     for num in item:
#         result.append(num + matrix2[outerIndex][innerIndex])
#         innerIndex += 1
#     outerIndex += 1
#
# print(result)

###############################################################################
# 11 De-dup
# Given an list of numbers or strings, create a new list containing the same
# elements as the first list, except with any duplicate values removed. Print the list.

# string1 = ['Jim', 'Bob', 'Alex', 'Josh', 'Mike', 'Billy']
# string2 = ['Jim', 'Bob', 'Jen', 'Eric', 'Mike', 'Billy']
#
# for str in string2:
#     if str in string1:
#         string1.remove(str)
# print(string1)

###############################################################################
# Bonus
# Given two two-dimensional lists of numbers of the size 2x2 - calculate the
# result of multiplying the two matrices. Print the resulting matrix. How do you
# multiple two matricies?
# https://www.khanacademy.org/math/precalculus/precalc-matrices/multiplying-matrices-by-matrices/v/matrix-multiplication-introß

x = [[1,5,4],[2,3,6],[4,8,9]]
y = [[2,9,3],[4,8,1],[5,7,6]]

r = []

for i in range(len(x)):
    n = []
    for j in range(len(x)):
        z = 0
        for k in range(len(x)):
            xx = x[k]
            yy = y[j]
            z += xx[j] * yy[k]
        n.append(z)
    r.append(n)

print(r)
