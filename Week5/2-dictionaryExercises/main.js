// Exercise 1

// var phonebookDict = {
//     Alice: '703-493-1834',
//     Bob: '857-384-1234',
//     Elizabeth: '484-584-2923'
// };

// console.log(phonebookDict.Elizabeth);
// phonebookDict.Kareem = '938-489-1234';
// console.log(phonebookDict.Kareem);
// delete phonebookDict.Alice;
// console.log(phonebookDict.Alice);
// phonebookDict.Bob = '968-345-2345';
// console.log(phonebookDict.Bob);

// var personName = 'Elizabeth';
// console.log(phonebookDict[personName]);

// for (name in phonebookDict){
//     console.log(name);
// };

// Letter Histogram

// function letterHistogram(word){
//     wordDict = {}
//     for (index in word){
//         if (word[index] in wordDict){
//             wordDict[word[index]] += 1;
//         }
//         else {
//             wordDict[word[index]] = 1;
//         }
//     }
//     return wordDict;
// };

// console.log(letterHistogram('bananas'));

// Word Histogram

// function wordHistogram(words){
//     wordArr = words.split(" ");
//     wordDict = {};
//     for (index in wordArr){
//         if (wordArr[index] in wordDict){
//             wordDict[wordArr[index]] += 1;
//         }
//         else {
//             wordDict[wordArr[index]] = 1;
//         }
//     }
//     return wordDict;
// };

// console.log(wordHistogram('to be or not to be'))

// Bonus

function letterHistogram(word){
    wordDict = {};
    for (index in word){
        if (word[index] in wordDict){
            wordDict[word[index]] += 1;
        }
        else {
            wordDict[word[index]] = 1;
        }
    }

    // Transfer values into an Array
    wordArr = [];
    for (key in wordDict){
        wordArr.push(wordDict[key]);
    }

    // Sort the values from highest to lowest
    isSorted = wordArr.sort(function(a, b){
        return b - a;
    });

    // Return the top 2 most used letters
    top2Resuts = [];
    for (var i = 0; i < 2; i++){
        top2Resuts[i] = isSorted[i];
    }
    return top2Resuts;
};

console.log(letterHistogram('bananas'));
