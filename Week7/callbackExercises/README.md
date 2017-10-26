# Callback Exercises

## Function Rewrites

Rewrite the following normal functions into callback functions.
```
function add(x, y) {
  var result = x + y;
  return result;
}

function subtract(x, y) {
  return x - y;
}

function greeting(person) {
  return 'Hola, ' + person + '!';
}

function product(numbers) {
  return numbers.reduce(function(a, b) {
    return a * b;
  }, 1);
}
```

## Function Rewrites with a Delay

Add a 1000 millisecond delay to the callback versions of the exercise above.