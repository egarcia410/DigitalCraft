const index = require("./index");

var url = 'http://css-tricks.com';
var filename = 'css-tricks.html';
console.log(index);

index.saveWebPage(url, filename, function (err) {
    if (err) {
        console.log(err.message);
        return;
    }
    console.log('It worked.');
});