# Promise Exercises

## Web Scraping

Given an array of urls:
```
var urls = [
  'https://en.wikipedia.org/wiki/Futures_and_promises',
  'https://en.wikipedia.org/wiki/Continuation-passing_style',
  'https://en.wikipedia.org/wiki/JavaScript',
  'https://en.wikipedia.org/wiki/Node.js',
  'https://en.wikipedia.org/wiki/Google_Chrome'
];
```
Use Promise.all and request-promise to retrieve the HTML files for all the web pages.

## Chaining

Using request-promise and fs-promise modules build a function called saveWebPage which takes two parameters, url and filename. The function should chain the two promises together to download the URL and then save the file.

## Cat 2 Files

Write a function that takes two input filenames and one output filename. Read the files and combine the file contents. Write the combined contents to the output file. Use a promise style to chain the reading and writing together.

## Resolve, Reject

Write a promise that adds two numbers and resolves the answer. However, if the two inputs provided are not both numbers reject the promise. The API should work like the following:
```
addNumbers(x, y)
  .then(function (answer) {
    console.log(answer);
  })
  .catch(function (error) {
    console.log(error);
  });
```

## Bonus: Cat N Files

Rewrite the 2 file concatenator so that it accepts a list of an arbitrary number of filenames and one output filename. Use a promise style to chain the reading and write together.