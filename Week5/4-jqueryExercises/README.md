# jQuery Exercises

## Exercise 1
```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title></title>
    <script src="jquery.js"></script>
    <script>
    /*
    Change the text of the button to "Please click me!". Putting your code in the document ready block is important.
    */
    $(document).ready(function () {
      // Put your code here
    });
    </script>
  </head>
  <body>
    <button id="the-button">meh</button>
  </body>
</html>
```
## Exercise 2
```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title></title>
    <script src="jquery.js"></script>
    <script>
    /*
    When the button is clicked, print "You clicked!" to the console. */
    $(document).ready(function () {
      // Put your code here
    });
    </script>
  </head>
  <body>
    <button id="the-button">Click me!</button>
  </body>
</html>
```
## Exercise 3
```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title></title>
    <script src="jquery.js"></script>
    <script>
    /*
    When the button is clicked, change the text of the paragraph #the-message to "You clicked me!", and the text of the button #the-button to "Click again?".
    */
    </script>
  </head>
  <body>
    <p id="the-message">Pardon me, would you please</p>
    <button id="the-button">Click me?</button>
  </body>
</html>
```
## Exercise 4
```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title></title>
    <script src="jquery.js"></script>
    <script>
    /*
    When the clear button is clicked, clear the text field.
    When the save button is clicked, take the text value inside the text field, and append a new <li> element to the #log with the entered text value.
    */
    $(function () {
      // write your code here
    });
    </script>
  </head>
  <body>
    <input id="text-field" type="text" name="text">
    <button id="clear-button">Clear</button>
    <button id="save-button">Save</button>
    <ul id="log">
      <li>Type messages here:</li>
    </ul>
  </body>
</html>
```
## Exercise 5
```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Todo List Exercise</title>
    <script src="jquery.js"></script>
    <script>
    /*
    Make it so that when you click on one of the links on this page,
    instead of navigating the browser to that page, it renders that
    page in the iframe below. Set the iframe's `src` attribute to a URL will cause it to render the page.
    */
    $(function() {
      // Write code here
    });
    </script>
  </head>
  <body>
    <ul>
      <li><a href="http://hellohappy.org">Hello Happy</a></li>
      <li><a href="http://duckduckgo.com">DuckDuckGo</a></li>
      <li><a href="http://css-tricks.com">CSS Tricks</a></li>
    </ul>
    <iframe id="iframe" src="http://hellohappy.org" width="800" height="480"></iframe>
  </body>
</html>
```
## Exercise 6
```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Todo List Exercise</title>
    <script src="jquery.js"></script>
    <script>
    /*
    Make the hide the section the first time the section header is clicked, show it when it is clicked again.
    */
    $(function() {
      // Write code here
    });
    </script>

    <style>
    #section-header {
      background-color: blue;
      color: white;
      padding: 5px;
    }
    #accordion {
      width: 400px;
      background-color: yellow;
      margin: auto;
    }
    #section {
      padding: 5px;
    }
    </style>
  </head>
  <body>
    <div id="accordion">
      <h3 id="section-header">Section 1</h3>
      <div id="section">
        <p>
        Mauris mauris ante, blandit et, ultrices a, suscipit eget, quam. Integer
        ut neque. Vivamus nisi metus, molestie vel, gravida in, condimentum sit
        amet, nunc. Nam a nibh. Donec suscipit eros. Nam mi. Proin viverra leo ut
        odio. Curabitur malesuada. Vestibulum a velit eu ante scelerisque vulputate.
        </p>
      </div>
    </div>
  </body>
</html>
```