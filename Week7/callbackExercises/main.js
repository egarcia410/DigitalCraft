function add(x, y, callback) {
    var result = x + y;
    callback(result);
  }

add(1, 2, function(result){
    console.log(result, "Add");
});
  
function subtract(x, y, callback) {
    var result = x - y;
    callback(result)
}

subtract(1, 2, function(result){
    console.log(result, "Subtract");
});
  
function greeting(person, callback) {
    callback(person);
};

greeting("Emmanuel", function(person){
    console.log(`Hola, ${person}!`)
});
  
function product(numbers, callback) {
    callback(numbers);
};

product([3, 1, 5, 9, 25], function(numbers){
    setTimeout(function(){
        console.log(numbers.reduce(function(a, b){
            return a* b;
        }));
    }, 1000);
});
