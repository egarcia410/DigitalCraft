# Express Exercises

## Hello World

Make an express program that will display `"Hello, world!"` at the root URL: `/`

## Routes

Add to your program the following pages:

* "Meow" at the URL `/cats`
* "Woof" at the URL `/dogs`
* "Living together" at the URL `/cats_and_dogs`


## Route Parameters

Adding to the same program, say a greeting to the user, given that the user's name is encoded inside the URL. For example, if you go to the URL

* `/greet/Kennedy` it should say "Hello, Kennedy!"
* `/greet/Jamison` it should say "Hello, Jamison!"
* `/greet/Manny` it should say "Hello, Manny!"
* etc...

## Query Parameters: Tell the year you were born

Adding to the same program, display the year you were born when you report your age in a query parameter. For example, when you go to the URL:

* `/year?age=32` it will display `You were born in 1985.`

## Templates

Make the greet page say hello to visitor and tell the year they were born. This time you will use a .hbs file in the views folder to render the message using HTML.

For example, if you go to the URL:

`/greet/Manoush?age=32`

The server should render the html:
```
<h1>Hello, Manoush!</h1>
<p>You were born in 1985.</p>
```

## Templates 2

Create this array in your server program:
```
var animals = [
  { name: 'cats', favorite: true },
  { name: 'dogs', favorite: true },
  { name: 'tree frogs', favorite: true },
  { name: 'earth worms', favorite: false },
  { name: 'guinea pigs', favorite: true },
];
```
**Feel free to change to match your current state of mind.**

Create a page at the URL `/fav_animals` that will render an ordered list of those animals which are your favorite.

## Templates 3

Go back through each page you have created previous and make an .hbs for each one, use resp.render to render them.

## The Layout Template

Create a `layout.hbs` file in the views folder. This will become the layout for all the pages. You will put `<html>` and `<body>` elements in here, while including a `{{{body}}}` placeholder which will bring in the content of each page.

## Static Files

Create a `public` folder in your project. Setup express to serve up all files within the public folder. Create a `style.css` in it, and then link to it in your `layout.hbs`. Using CSS to give all your pages a common theme.
