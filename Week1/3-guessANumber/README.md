# Guess a Number

### Step 1

You will implement a guess-the-number game where the player has to try guessing a secret number until he gets it right. For now, you will "hard code" the secret number to 5 (just set it to five like secret_number = 5). You will prompt the player to enter a number again and again, each time comparing his input to the secret number. To to that, you will need to write a while loop. If he guesses correctly, you will print "You win!", otherwise, you will prompt for a number again.

Example session:
```
$ python guess_the_number.py
I am thinking of a number between 1 and 10.
What's the number? 3
Nope, try again.
What's the number? 9
Nope, try again.
What's the number? 5
Yes! You win!
```
### Step 2: Give High-Low Hint

Improve your game to provide the player with a high-or-low hint. Example session:
```
$ python guess_the_number.py
I am thinking of a number between 1 and 10.
What's the number? 3
3 is too low.
What's the number? 9
9 is too high.
What's the number? 5
Yes! You win!
```
### Step 3: Randomly Generated Secret Number

Instead of hard-coding the secret number to 5 now, you will generate the secret number using a random number generator provided by Python, so that even you, the programmer, cannot know the secret number before hand. To generate a random number between 1 and 10, inclusive, do this:
```
import random
my_random_number = random.randint(1, 10)
```
Use this same method to generate your secret number for the game. Play the game a couple of times to see that the secret number is different each time.

### Step 4: Limit Number of Guesses

Limit the number of guesses the player has to 5. If he cannot guess the number within 5 guesses, he losses. Example session:
```
$ python guess_the_number.py
I am thinking of a number between 1 and 10.
You have 5 guesses left.
What's the number? 1
1 is too low.
You have 4 guesses left.
What's the number? 10
10 is too high.
You have 3 guesses left.
What's the number? 2
2 is too low.
You have 2 guesses left.
What's the number? 7
7 is too high.
You have 1 guesses left.
What's the number? 4
4 is too low.
You ran out of guesses!
```
### Bonus: Play Again

At the conclusion of a game, give the player the option of playing again. Example session:
```
$ python guess_the_number.py
I am thinking of a number between 1 and 10.
You have 5 guesses left.
What's the number? 1
Yes! You win!
Do you want to play again (Y or N)? Y
I am thinking of a number between 1 and 10.
You have 5 guesses left.
What's the number? 5
Yes! You win!
Do you want to play again (Y or N)? N
Bye!
```
