# 1 FizzBuzz
# for num in range(1, 101):
#     if num % 3 == 0 and num % 5 == 0:
#         print(num, 'FizzBuzz')
#     elif num % 5 == 0:
#         print(num, 'Buzz')
#     elif num % 3 == 0:
#         print(num, 'Fizz')
#     else:
#         print(num)

# 2
# mult = []
#
# for num in range(3, 1000):
#     if num % 3 == 0:
#         mult.append(num)
#
# for num in range(5, 1001):
#     if num % 5 == 0:
#         mult.append(num)
#
# removeDup = list(set(mult))
#
# print(sum(removeDup))

# 3 Fibonacci
# def fib():
#
#     total = 2
#     temp1 = 1
#     temp2 = 2
#     # max is true if under 4,000,000
#     while total < 4000001:
#         temp = temp1
#         temp1 = temp2
#         temp2 = temp + temp1
#         if temp2 % 2 == 0:
#             total += temp2
#     return total
#
# print(fib())

# 4 Prime Factors
# NOT EFFICIENT
# largestPrime = 0
# for num in range(1, 5):
#     for num2 in range(2, num + 1):
#         if num % num2 == 0:
#             if num2 != num:
#                 break
#             else:
#                 largestPrime = num2
# print(largestPrime)

# 5
# primeCount = 0
# prime = 1
# while primeCount != 100:
#     for num in range(1, 100):
#         primeCount += 1
#         for num2 in range(2, num + 1):
#             if num % num2 == 0:
#                 if num2 != num:
#                     break
#                 else:
#                     prime = num2
# print(prime)
