const express = require('express');
const app = express();
const hbs = require('hbs');
const port = 8000;

// Create a virtual path prefix for static files
app.use('/static', express.static('public'))
// Directory for the application's views
app.set('views', './public/views');
// hbs as the default view engine
app.set('view engine', 'hbs');

app.get('/', function(req, res) {
    res.render('index');
})

app.listen(port, function () {
    console.log(`Creating magic on port ${port}`);
});