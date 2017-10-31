// Use the marked module
// const marked = require('marked');

// console.log(marked('I am using __markdown__.'));

// Lodash
// Load the full build.
// const _ = require('lodash');

// numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

// console.log(_.shuffle(numbers));

// Bonus: Request and Cheerio
const cheerio = require('cheerio');
const request = require('request');

const $ = cheerio.load(
    request('https://www.npmjs.com/', function (error, response, html) {
        const $ = cheerio.load(html);
        const packageArr = [];
        $("h3 > a.type-neutral-1").each(function(i, elem){
            packageArr[i] = $(this).text();
        });
        console.log(packageArr);
    })
);

// Bonus 2: Any module
// const cows = require('cows');

// for (var i = 0; i < cows().length; i++){
//     console.log(cows()[i]);
// }