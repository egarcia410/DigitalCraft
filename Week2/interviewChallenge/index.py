# Challenge 1
# numList = []
# def collatz(num):
#     numList.append(num)
#     if num == 1:
#         return numList
#     if  num % 2 == 0:
#         num = num / 2
#         return collatz(num)
#     else:
#         num = (num * 3) + 1
#         return collatz(num)
# print(collatz(20))

# Challenge 2
# def largestPal():
#     for i in range(999, 99, -1):
#         for j in range(999, 99, -1):
#             num = j * i
#             numReverse = int("".join(list(str(num))[::-1]))
#             if num == numReverse:
#                 return num
# print(largestPal())

# Challenge 3
# def divisible():
#     divisible = False
#     num = 10
#     while not divisible:
#         numList = []
#         for x in range(3, 20):
#             print(num)
#             if num % x == 0:
#                 numList.append(x)
#             if len(numList) == 17:
#                 return num
#         num += 10

# print(divisible())
                