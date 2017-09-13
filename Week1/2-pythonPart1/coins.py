coins = 0
print('You have {} coins.'.format(coins))

# res = input('Do you want another? ').lower()
#
# while res != 'yes':
#     res = input('Do you want another? ').lower()
#
# while res == 'yes':
#     coins += 1
#     print('You have {} coins.'.format(coins))
#     res = input('Do you want another? ').lower()
#     while res != 'yes':
#         if res == 'no':
#             print('Bye')
#             break
#         res = input('Do you want another? ').lower()

while True:
    res = input('Do you want another? ').lower()
    if res == 'yes':
        coins += 1
        print('You have {} coins.'.format(coins))
    elif res == 'no':
        print('Bye')
        break
    else:
        print('Try again')
