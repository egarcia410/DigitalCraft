# Step 1
# secret_number = 5
#
# print('I am thinking of a number between 1 and 10.')
# num = int(input('What\'s the number? '))
#
# while True:
#     if num == secret_number:
#         print('Yes! You Win!')
#         break
#     else:
#         print('Nope, try again')
#         num = int(input('What\'s the number? '))

# #############################################################################
# Step 2 Give High-Low Hint
# secret_number = 5
#
# print('I am thinking of a number between 1 and 10.')
# num = int(input('What\'s the number? '))
#
# while True:
#     if num == secret_number:
#         print('Yes! You Win!')
#         break
#     elif num < secret_number:
#         print('{} is too low'.format(num))
#         num = int(input('What\'s the number? '))
#     elif num > secret_number:
#         print('{} is too high'.format(num))
#         num = int(input('What\'s the number? '))


# #############################################################################
# Step 3 Randomly Generated Secret Number
# import random
# secret_number = random.randint(1,10)
#
# print('I am thinking of a number between 1 and 10.')
#
# while True:
#     num = int(input('What\'s the number? '))
#     if num == secret_number:
#         print('Yes! You Win!')
#         break
#     elif num < secret_number:
#         print('{} is too low'.format(num))
#     elif num > secret_number:
#         print('{} is too high'.format(num))

# #############################################################################
# Step 4 & Bonus Limit Number of Guesses & Play Again
import random
secret_number = random.randint(1,10)
turns = 5

print('I am thinking of a number between 1 and 10.')
print('You have {} guesses left'.format(turns))

def playAgain():
    while True:
        res = input('Do you want to play again (Y or N)? ').lower()
        if res == 'y':
            secret_number = random.randint(1,10)
            print('I am thinking of a number between 1 and 10.')
            print('You have {} guesses left'.format(turns))
            play(turns, secret_number)
        elif res == 'n':
            return
        else:
            print('Please enter valid response')

def play(turns, secret_number):
    while turns:
        try:
            num = int(input('What\'s the number? '))
        except ValueError:
            print('Please enter a number')
            continue
        if num == secret_number:
            print('Yes! You Win!')
            playAgain()
            return
        elif num < secret_number:
            turns -= 1
            print('{} is too low'.format(num))
            if turns == 0:
                print('You ran out of guesses!')
                playAgain()
                return
            print('You have {} guesses left'.format(turns))
        elif num > secret_number:
            turns -= 1
            print('{} is too high'.format(num))
            if turns == 0:
                print('You ran out of guesses!')
                playAgain()
                return
            print('You have {} guesses left'.format(turns))

play(turns, secret_number)
