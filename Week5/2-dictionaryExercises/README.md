# Object as Dictionary Exercises

## Exercise 1

Given the following dictionary, representing a mapping from names to phone numbers:
```
var phonebookDict = {
  Alice: '703-493-1834',
  Bob: '857-384-1234',
  Elizabeth: '484-584-2923'
}
```
Write code to do the following:

1. Print Elizabeth's phone number.
2. Add a entry to the dictionary: Kareem's number is 938-489-1234.
3. Delete Alice's phone entry.
4. Change Bob's phone number to '968-345-2345'.
5. Given this code var personName = 'Elizabeth';, use the variable personName to access the dictionary entry. 
6. Use a for...in loop to print all the phone entries.

## Letter Histogram

Write a function letterHistogram which takes a string as argument. It will tally(histogram) the number of times each character appears in the string, and return the tally as an object. Example:
```
> letterHistogram('bananas')
{ b: 1, a: 3, n: 2, s: 1 }
```
**Note: the order of the keys doesn't matter.**

## Word Histogram

Write a function wordHistogram which takes a string as argument and tallies the number of times each word appears in the string, and returns the tally as an object. Example:
```
> wordHistogram('to be or not to be')
{ to: 2, be: 2, or: 1, not: 1 }
```

## Bonus

Print the top 2 most frequently used letters in the string from the letter histogram exercise.