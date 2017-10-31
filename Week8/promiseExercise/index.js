// Web Scraping
// var rp = require('request-promise');
// var cheerio = require('cheerio'); // Basically jQuery for node.js


// var urls = [
//     'https://en.wikipedia.org/wiki/Futures_and_promises',
//     'https://en.wikipedia.org/wiki/Continuation-passing_style',
//     'https://en.wikipedia.org/wiki/JavaScript',
//     'https://en.wikipedia.org/wiki/Google_Chrome',
//     'https://en.wikipedia.org/wiki/Node.js'
// ];

// function getURLs(){
//     return urls.map(function(url){
//         rp(url)
//             .then(function (htmlString) {
//                 console.log(htmlString);
//             })
//             .catch(function (err) {
//                 console.log(err);
//             });
//     })
// }

// Promise.all(getURLs())
//     .then(function(response){
//         console.log(response);
//     })
//     .catch(function(error){
//         console.log(error);
//     });

// Chaining
// const rp = require('request-promise');
// const cheerio = require('cheerio');
// const readline = require('readline');
// const fs = require('fs');

// const rl = readline.createInterface({
//     input: process.stdin,
//     output: process.stdout
// });

// rl.question('URL Name: ', (url) => {
//     rl.question('Filename: ', (filename) => {
//         let options = {
//             uri: url,
//             transform: function (body) {
//                 return cheerio.load(body);
//             }
//         };
//         rp(options)
//             .then(function ($) {
//                 let body = $('html').html();
//                 fs.writeFile(filename, body, function (error) {
//                     if (error) {
//                         console.error(error.message);
//                         return;
//                     }
//                     console.log('File Saved: ', filename);
//                 });
//             })
//             .catch(function (err) {
//                 console.log(err.message);
//             });
//         rl.close();
//     });
// });

// Cat 2 Files
// const fs = require('fs');
// const readline = require('readline');

// function readFiles(filename){
//     var promise = new Promise(function(resolve, reject){
//         try {
//             fs.readFile(`./${filename}`, (err, data) => {
//                 if (err) {
//                     console.log(err.message);
//                 }
//                 resolve(data.toString())
//             });
//         } catch (error) {
//             reject(error)
//         }
//     });
//     return promise
// }

// const rl = readline.createInterface({
//     input: process.stdin,
//     output: process.stdout
// });

// rl.question('Filename 1: ', (filename1) => {
//     rl.question('Filename 2: ', (filename2) => {
//         rl.question('Output filename: ', (output) => {
//             Promise.all([readFiles(filename1), readFiles(filename2)])
//                 .then(function(response){
//                     fs.writeFile(`./${output}`, response, (err) => {
//                         if (err) {
//                             console.log(err.message);
//                         }
//                         console.log(`${filename1} and ${filename2} have been saved to ${output}`)
//                     })
//                 })
//                 .catch(function(err){
//                     console.log(err);
//                 });
//             rl.close();
//         })
//     });
// });

// // Resolve, Reject
// function addNumbers(num1, num2){
//     let promise = new Promise(function(resolve, reject){
//         try {
//             if (typeof num1 !== 'number' || typeof num2 !== 'number') {
//                 throw new Error('Invalid input, please enter a number');
//             }
//             resolve(num1 + num2);
//         } catch(error) {
//             reject(error)
//         }
//     });
//     return promise;
// }

// addNumbers(1, true)
//     .then(function(response){
//         console.log(response);
//     })
//     .catch (function(error){
//         console.log(error.message);
//     })

// Bonus: Cat N Files
const fs = require('fs');
const readline = require('readline');

function readFiles(arr){
    let results = arr.map(function(data){
        let promise = new Promise(function(resolve, reject){
            try {
                fs.readFile(`./${data}`, (err, data) => {
                    if (err) {
                        reject(err);
                    } 
                    resolve(data.toString());
                });
            } catch (err) {
                reject(err);
            }
        });
        return promise;
    });
    return results;
}

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let isFilename = true;
let arrFilenames = [];

let recursiveReadLine = function() {
    rl.question('Filename: ', (filename) => {
        arrFilenames.push(filename);
        rl.question('Continue with another filename? (Y/N): ', (response) => {
            if (response.toLowerCase() === 'n') {
                outputFile();
                return;
            }
            recursiveReadLine();
        });
    });
}

recursiveReadLine();

function outputFile() {
    rl.question('Output filename: ', (output) => {
        Promise.all(readFiles(arrFilenames))
            .then(function(response){
                fs.writeFile(`./${output}`, response, (err) => {
                    if (err) {
                        console.log(err.message);
                    }
                    console.log(`Files have been saved to ${output}`)
                })
            })
            .catch(function(err){
                console.log(err);
            });
            rl.close();
    });
}

