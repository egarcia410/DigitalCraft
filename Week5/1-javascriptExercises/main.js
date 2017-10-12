// Madlib
// function madlib(name, subject){
//     return `${name}'s favorite subject in school is ${subject}.`
// }

// console.log(madlib('Emmanuel', 'History'))

// Tip Calculator
// function tipCalc(amount, service){
//     tip = 0;
//     if (service.toLowerCase() === 'good') {
//         tip = .20;
//     }
//     else if (service.toLowerCase() === 'fair') {
//         tip = .15;
//     }
//     else if (service.toLowerCase() === 'bad') {
//         tip = .10;
//     }
//     return amount * tip;
// }

// console.log(tipCalc(100, 'bad'))

// Tip Calculator 2
// function tipAmount(amount, service){
//     tip = 0;
//     if (service.toLowerCase() === 'good') {
//         tip = .20;
//     }
//     else if (service.toLowerCase() === 'fair') {
//         tip = .15;
//     }
//     else if (service.toLowerCase() === 'bad') {
//         tip = .10;
//     }
//     return amount * tip;
// }

// function totalAmount(amount, service){
//     return tipAmount(amount, service) + amount
// }

// console.log(totalAmount(100, 'good'))

// Print Numbers
// function printNumbers(start, end){
//     for (var i = start; i <= end; i++){
//         console.log(i)
//     }
// }

// printNumbers(1, 10)

// Print a Square

// function printSquare(size){
//     pattern = []
//     for (var i = 0; i < size; i++){
//         console.log('*'.repeat(size))
//     }
// }

// printSquare(5)

// Print a Box

// function printBox(width, height){
//     boxStr = ""
//     for(var i = 0; i < height; i++){
//         if (i === 0 || i === height - 1){
//             boxStr += '*'.repeat(width)
//             if (i === height - 1) {
//                 console.log(boxStr)
//             }
//         }
//         else {
//             boxStr += "*" + (" ".repeat(width - 2)) + "*"
//         }
//         boxStr += '\n'
//     }
// }

// printBox(6, 10)

// Print a Banner

// function printBanner(word){
//     width = word.length + 4
//     boxStr = ""
//     for (var i = 0; i < 3; i++){
//         if (i === 0 || i === 2){
//             boxStr += '*'.repeat(width)
//             if (i === 2) {
//                 console.log(boxStr)
//             }
//         }
//         else {
//             boxStr += "* " + word + " *"
//         }
//         boxStr += '\n'
//     }
// }

// printBanner('Welcome to DigitalCrafts')

// Leetspeak

// function leetspeak(word){
//     arr = word.split("");
//     leetspeak = {
//         'A': 4,
//         'E': 3,
//         'G': 6,
//         'L': 1,
//         'O': 0,
//         'S': 5,
//         'T': 7
//     };
//     arr.forEach(function(letter, index) {
//         if (letter.toUpperCase() in leetspeak){

//             arr[index] = leetspeak[letter.toUpperCase()]
//         };
//     });
//     return arr.join("")
// }

// console.log(leetspeak('Leet'))

// Just the Positives

// function positiveNumbers(arr){
//     newArr = [];
//     arr.forEach(function(num) {
//         if (num >= 0){
//             newArr.push(num)
//         }
//     });
//     return newArr;
// };

// console.log(positiveNumbers([1, -3, 5, -3, 0]))

// Caesar Cipher

// function cipher(word, offset){
//     newStr = ""
//     for (var i = 0; i < word.length; i++){
//         // passes an spaces in the string
//         if (word[i] == " "){
            
//         }
//         letterToNum = (word).charCodeAt(i);
//         // if letterToNum is an uppercase letter
//         if (letterToNum >= 65 && letterToNum <= 90){
//             letterToNumOffset = letterToNum + offset;
//             if (letterToNumOffset > 116){
//                 remainder = offset % 26;
//                 letterToNum = letterToNum + remainder - 26;
//             }
//             else if (letterToNumOffset <= 90) {
//                 letterToNum = letterToNumOffset;
//             }
//             else {
//                 letterToNum = letterToNumOffset - 26;
//             }
//         }
//         // if letterToNum is a lowercase letter
//         else if (letterToNum >= 97 && letterToNum <= 122){
//             letterToNumOffset = letterToNum + offset;
//             if (letterToNumOffset > 148){
//                 remainder = offset % 26;
//                 letterToNum = letterToNum + remainder - 26;
//             }
//             else if (letterToNumOffset <= 122) {
//                 letterToNum = letterToNumOffset;
//             }
//             else {
//                 letterToNum = letterToNumOffset - 26;
//             }
//         }
//         numToLetter = String.fromCharCode(letterToNum);
//         newStr += numToLetter;
//     }
//     return newStr
// }

// console.log(cipher('Genius without education is like silver in the mine', 13))

// Caesar Cipher 2

function cipher(word, offset){
    newStr = ""
    for (var i = 0; i < word.length; i++){
        // passes an spaces in the string
        if (word[i] == " "){
            
        }
        letterToNum = (word).charCodeAt(i);
        // if letterToNum is an uppercase letter
        if (letterToNum >= 65 && letterToNum <= 90){
            letterToNumOffset = letterToNum - offset;
            if (letterToNumOffset < 39){
                remainder = offset % 26;
                letterToNum = letterToNum - remainder + 26;
            }
            else if (letterToNumOffset >= 65) {
                letterToNum = letterToNumOffset;
            }
            else {
                letterToNum = letterToNumOffset + 26;
            }
        }
        // if letterToNum is a lowercase letter
        else if (letterToNum >= 97 && letterToNum <= 122){
            letterToNumOffset = letterToNum - offset;
            if (letterToNumOffset < 71){
\                remainder = offset % 26;
                letterToNum = letterToNum - remainder + 26;
            }
            else if (letterToNumOffset >= 97) {
                letterToNum = letterToNumOffset;
            }
            else {
                letterToNum = letterToNumOffset + 26;
            }
        }
        numToLetter = String.fromCharCode(letterToNum);
        newStr += numToLetter;
    }
    return newStr
}

console.log(cipher('Travhf jvgubhg rqhpngvba vf yvxr fvyire va gur zvar', 39))