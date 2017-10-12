# Function Exercises

Implement all of the following problems without using a while or a for loop unless you were explicitly asked to use loops.

## Even Numbers

Write a function which takes an array of numbers as input and returns a new array containing only the even numbers in the given array.

## Square the Numbers

Write a function which takes an array of numbers as input and returns a new array containing result of squaring each of the numbers in the given array by two. Example: `squareTheNumbers([1, 2, 3])` should give `[1, 4, 9]`.

## Cities

Write a function which takes an array of city objects like such:
```
var cities = [
  { name: 'Los Angeles', temperature: 60.0},
  { name: 'Atlanta', temperature: 52.0 },
  { name: 'Detroit', temperature: 48.0 },
  { name: 'New York', temperature: 80.0 }
];
```
as input and returns a new array containing the cities whose temperature is cooler than 70 degrees.

## Good Job!

Given an array of people's names:
```
var people = [
  'Dom',
  'Lyn',
  'Kirk',
  'Autumn',
  'Trista',
  'Jesslyn',
  'Kevin',
  'John',
  'Eli',
  'Juan',
  'Robert',
  'Keyur',
  'Jason',
  'Che',
  'Ben'
];
```
Print out `'Good Job, {{name}}!'` for each person's name, one on a line.

## Sort an array

Given an array of strings such the array of names given in the previous problem, sort them by alphabetically order.

## Sort an array, 2

Sort the same array, but not by alphabetically order, but by how long each name is, shortest name first.

## 3 times

Given this function:
```
function call3Times(fun) {
  fun();
  fun();
  fun();
}
```
Use the `call3Times` function to print "Hello, world!" 3 times.

## n times

You will write a function callNTimes that takes two arguments: times as a number, and fun as a function. It will call that function for that many times. Example:
```
> callNTimes(5, hello)
Hello, world!
Hello, world!
Hello, world!
Hello, world!
Hello, world!
```
You are allowed to use a loop in the implementation of `callNTimes`.

## Sum an array

Write a function sum that takes an array of numbers as argument and returns the sum of those numbers. Use the reduce method to do this.
```
> sum([1, 2, 3])
6
```

## Acronym

Write a function acronym that takes an array of words as argument and returns the acronym of the words. Use the reduce method to do this.
```
> acronym(['very', 'important', 'person'])
'VIP'
> acronym(['national', 'aeronautics', 'space', 'administration'])
'NASA'
```

## Bonus: forEach

Implement your own custom forEach function which takes two arguments: an array arr and a function fun. It will call fun passing each item in arr to fun as the first argument. Example:
```
var arr = [
  { name: 'Bob' },
  { name:'Alice' },
  { name:'Joe' }
];

forEach(arr, function(person) {
  console.log('Hello, ' + person.name + '!');
});
```
The above program will print:
```
Hello, Bob!
Hello, Alice!
Hello, Joe!
```
You can use a loop in the implementation of this function.

## Bonus: map

Implement your own custom map function which takes two arguments: an array arr and a function fun. It will return a new array, with each of its results being the result of calling fun with each array element.

## Bonus: Caesar Cipher

Rewrite this cipher function without using a loop, using the help of array's map, join, and string's split method.
```
function cipher(text) {
  var alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split('');
  var result = '';
  for (var i = 0; i < text.length; i++) {
    var chr = text[i];
    var idx = alphabet.indexOf(chr.toUpperCase());
    var newIdx = idx + 13;
    if (newIdx >= alphabet.length) {
      newIdx -= 26;
    }
    result += alphabet[newIdx];
  }
  return result;
}

// You can assume that the text is only one word, all letters are capitalized, and the offset is always 13
var encrypted = cipher('GENIUS');

console.log(encrypted);
```