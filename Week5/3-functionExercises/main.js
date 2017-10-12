// Even Numbers

// function evenNumbers(arr){
//     return arr.filter(x => x % 2 === 0)
// };

// console.log(evenNumbers([1,5,7,8,9,4,2]))

// Square the Numbers

// function squareNumbers(arr){
//     return arr.map(x => x * x)
// };

// console.log(squareNumbers([1,5,7,8,9,4,2]))

// Cities

// var cities = [
//     { name: 'Los Angeles', temperature: 60.0},
//     { name: 'Atlanta', temperature: 52.0 },
//     { name: 'Detroit', temperature: 48.0 },
//     { name: 'New York', temperature: 80.0 }
//   ];

//   function coolCities(cities){
//       return cities.filter(x => x.temperature < 70);
//   }

//   console.log(coolCities(cities));


// Good Job!

// var people = [
//     'Dom',
//     'Lyn',
//     'Kirk',
//     'Autumn',
//     'Trista',
//     'Jesslyn',
//     'Kevin',
//     'John',
//     'Eli',
//     'Juan',
//     'Robert',
//     'Keyur',
//     'Jason',
//     'Che',
//     'Ben'
//   ];

// function goodJob(people){
//     return people.forEach(function(name) {
//         console.log(`Good Job, ${name}!`);
//     }, this);
// };

// goodJob(people);

// Sort an Array

// function sortPeople(people){
//     return people.sort();
// };

// console.log(sortPeople(people));

// Sort an Array 2
// Use people array from previous problem 

// function sortPeople(people){
//     return people.sort(function(a,b){
//         return b.length - a.length;
//     });
// };

// console.log(sortPeople(people));

// 3 Times

// function call3Times(fun) {
//     fun();
//     fun();
//     fun();
//   }

// var fun = function(){
//     console.log("Hello, World!");
// };

// call3Times(fun);

// n Times

// var hello = function(){
//     console.log('Hello, World!');
// };

// function callNTimes(num, hello){
//     for (var i = 0; i < num; i++){
//         hello()
//     }
// };

// callNTimes(7, hello);

// Sum and Array

// function sum(arr){
//     return arr.reduce(function(a, b){
//         return a + b;
//     });
// };

// console.log(sum([1,2,3,4,5]));

// Acronym

// function acronym(arr){
//     newArr = []
//     return arr.reduce(function(total, currentVal, currentIndex){
//         if (currentIndex === 1){
//             return total[0] + currentVal[0];
//         }
//         return total + currentVal[0];
//     });
// };

// console.log(acronym(['national', 'aeronautics', 'space', 'administration']));

// Bonus: Caesar Cipher

function cipher(text) {
    var arr = Array.from(text);
    var alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split('');
    return arr.map(function(currentVal, index){
        var chr = text[index];
        var idx = alphabet.indexOf(chr.toUpperCase());
        var newIdx = idx + 13;
        if (newIdx >= alphabet.length) {
          newIdx -= 26;
        }
        return alphabet[newIdx];
    });
}
  
// You can assume that the text is only one word, all letters are capitalized, and the offset is always 13
var encrypted = cipher('GENIUS');

console.log(encrypted);


