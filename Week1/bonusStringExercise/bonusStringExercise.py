# Guess Game 2
import random

print('Pick a number between 0 and 100')
print('The computer will attempt to guess your number')

attempts = 0
low = 0
high = 100
num = random.randint(low, high)

while True:
    print('Is your number ' + str(num) + '?')
    response = input('Yes(Y), Higher(H), or Lower(L)?').lower()
    if (low + 1) == high:
        print('Don\'t lie! Your number is ' + str(num))
        print('Number of attempts: ' + str(attempts))
        break
    elif response == 'y':
        print('Your number is ' + str(num))
        print('Number of attempts: ' + str(attempts))
        break
    elif response == 'h':
        attempts += 1
        low = num
        num = int(((high - low) / 2) + low)
    elif response == 'l':
        attempts += 1
        high = num
        num = int((high - low) / 2 + low)
    else:
        print('Please enter valid number')
