"""File I/O Exercies"""
# def exercise1():
#     """Exercise 1: User inputs file name and read contents of file"""
#     response = input('Filename: ')
#     fname = response + '.txt'
#     with open(fname, 'w') as f:
#         f.write('This is the first line of the file.\n')
#         f.write('Second line of the file\n')
#     with open(fname, 'r') as f:
#         for line in f:
#             print(line, end='')

# exercise1()

# ############################################################################
# def exercise2():
#     """Exercise 2: User inpute file and contents, reads contents of file"""
#     response = input('Filename: ')
#     fname = response + '.txt'
#     with open(fname, 'w+') as f:
#         f.write('This is the first line of the file.\n')
#         f.write('Second line of the file\n')
#     with open(fname, 'r') as f:
#         for line in f:
#             print(line, end='')

# exercise2

# ############################################################################
# def exercise3():
#     """Exercise 3: Prints letter/word histogram of file contents"""
#     wordDict = {}
#     letterDict = {}
#     response = input('Filename: ')
#     fname = response + '.txt'
#     with open(fname, 'w+') as f:
#         f.write('This is the first line of the file.\n')
#         f.write('Second line of the file\n')
#     with open(fname, 'r') as f:
#         for line in f:
#             words = line.split(" ")
#             for word in words:
#                 word = word.lower()
#                 if word in wordDict:
#                     wordDict[word] += 1
#                 else: 
#                     wordDict[word] = 1
#             for letter in line:
#                 letter = letter.lower()
#                 if letter in letterDict:
#                     letterDict[letter] += 1
#                 else: 
#                     letterDict[letter] = 1
#     print('Word Histogram: ', wordDict)
#     print('Letter Histogram: ', letterDict)

# exercise3()

# ############################################################################
# import json
# import matplotlib.pyplot as plot

# def exercise4():
#     """Exercise 4: Takes a JSON file name as input and plots the X,Y data"""
#     data = { 'data': [
#                 [1, 1],
#                 [2, 2],
#                 [3, 3],
#                 [4, 4] ]
#             }
#     xCord = []
#     yCord = []
#     with open('data.json', 'w') as f:
#         json.dump(data, f)
#     with open('data.json', 'r') as f:
#         data = json.load(f)
#         for cord in data['data']:
#             xCord.append(cord[0])
#             yCord.append(cord[1])
    
#     plot.plot(xCord, yCord, 'ro')
#     plot.show()    

# exercise4()

# ############################################################################
# import sys

# def crashTest():
#     """Bonus Exercise: Write a program that writes to an in memory file until your program dies"""
#     text = ""
#     fh = open('hello.txt', 'w+')
#     while True:
#         text += 'a\n' 
#         fh.write(text)
#         content = fh.read()
#         print(sys.getsizeof(content))

# crashTest()
