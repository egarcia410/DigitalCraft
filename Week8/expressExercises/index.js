const express = require('express');
const app = express();
const port = 3000;

// Serve static files such as images, CSS files, and JavaScript files
// Create virtual path prefix, in this case '/static'
app.use('/static', express.static('public'))
// urlencoded defaults to qs library(true)
app.use(express.urlencoded({ extended: true }));
app.set('views', './public/views')
app.set('view engine', 'pug')

app.get('/', function (req, res) {
    content = {title: 'Home', message: 'Hello, World!'}
    res.render('index', content);
});

app.get('/cats', function (req, res) {
    content = { title: 'Cats', message: 'Meow' }
    res.render('index', content);
});

app.get('/dogs', function (req, res) {
    content = { title: 'Dogs', message: 'Woof!' }
    res.render('index', content);
});

app.get('/cats-and-dogs', function (req, res) {
    content = { title: 'Harmony', message: 'Living together' }
    res.render('index', content);
});

app.get('/greet/:name', function (req, res) {
    let name = req.params.name;
    let age = req.query.age;
    let year = new Date().getFullYear() - age;
    if (age) {
        content = { title: 'Greet', welcome: 'Hello, ' + name, message: 'You were born in ' + year }
    } else {
        content = { title: 'Greet', welcome: 'Hello, ' + name}
    }
    res.render('index', content);
});

app.get('/year', function (req, res) {
    let age = req.query.age;
    let year = new Date().getFullYear() - age;
    content = { title: 'Age', message: 'You were born in ' + year }
    res.render('index', content);
});

app.get('/fav-animals', function (req, res) {
    let animals = [
        { name: 'cats', favorite: true },
        { name: 'dogs', favorite: true },
        { name: 'tree frogs', favorite: true },
        { name: 'earth worms', favorite: false },
        { name: 'guinea pigs', favorite: true },
    ];
    content = { title: 'Animals', welcome: 'My Favorite Animals', animals: animals }
    res.render('index', content);
});

app.listen(port, function() {
    console.log(`Creating magic on port ${port}`);
});