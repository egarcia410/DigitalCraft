// #########################################################
// Read a file
// #########################################################

// var readline = require('readline');
// var fs = require('fs');

// var rl = readline.createInterface({
//     input: process.stdin,
//     output: process.stdout
// });
// rl.question("Enter a filename: ", function(filename) {
//     fs.readFile(filename, function (error, buffer) {
//         if (error) {
//           console.error(error.message);
//           return;
//         }
//         console.log(buffer.toString().toUpperCase());
//       });
//     rl.close();
// });

// #########################################################
// DNS lookup
// #########################################################

// const dns = require('dns');
// const readline = require('readline');

// const rl = readline.createInterface({
//     input: process.stdin,
//     output: process.stdout
// });

// rl.question("Enter a domain: ", function(domain) {
//     dns.lookup(domain, (err, address, family) => {
//     console.log('address: %j family: IPv%s', address, family);
//       });
//     rl.close();
// });

// #########################################################
// Read and Write
// #########################################################
// const readline = require('readline');
// const fs = require('fs');

// const rl = readline.createInterface({
//     input: process.stdin,
//     output: process.stdout
// });

// rl.question('Input file: ', (inputFile) => {
//     rl.question('Output file: ', (outputFile) => {
//         fs.readFile(inputFile, function (error, buffer) {
//             if (error) {
//                 console.error(error.message);
//                 return;
//             }
//             var contents = buffer.toString().toUpperCase();
//             fs.writeFile(outputFile, contents, function (error) {
//                 if (error) {
//                     console.error(error.message);
//                     return;
//                 }
//                 console.log('File Save: ', outputFile);
//             });
//         });
//         rl.close();
//     });
// });

// #########################################################
// Save a Web Page
// #########################################################
// const readline = require('readline');
// const fs = require('fs');
// // npm install request --save
// // https://www.sitepoint.com/web-scraping-in-node-js/
// const request = require("request");


// const rl = readline.createInterface({
//     input: process.stdin,
//     output: process.stdout
// });

// rl.question('Web Page: ', (webPage) => {
//     rl.question('Filename: ', (filename) => {
//         request({
//             uri: webPage,
//         }, function(error, response, body){
//             if (error) {
//                 console.log(error.message);
//                 return;
//             }
//             fs.writeFile(filename, body, function (error) {
//                 if (error) {
//                     console.error(error.message);
//                     return;
//                 }
//                 console.log('File Saved: ', filename);
//             });
//         });
//         rl.close();
//     });
// });

// #########################################################
// Resize an Image
// #########################################################
const http = require('https');
const fs = require('fs');
const request = require("request");
const sharp = require('sharp')

const options = {
    url: 'https://raw.githubusercontent.com/voodootikigod/logo.js/master/js.png',
    encoding: null
};

request(options, function (err, response, imageData) {
    sharp(imageData)
    .resize(240, 240)
    .toFile("./image.png", function(err, info){
        if (err){
            console.log(err.message);
            return;
        }
        console.log(info);
    });
});