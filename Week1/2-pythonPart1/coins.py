coins = 0
print('You have {} coins.'.format(coins))

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
