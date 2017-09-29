#Interview Challenge Week 3

### 1. CSS Shapes

[CSS Shapes](https://css-tricks.com/examples/ShapesOfCSS/)

In CSS you can produce different shapes via various hacks. For example a triangle pointing up can be produced with the following code:
```
#triangle-up {
  width: 0;
  height: 0;
  border-left: 50px solid transparent;
  border-right: 50px solid transparent;
  border-bottom: 100px solid red;
}
```
See what creative hacks you can do to get the following shapes without Googling the entire shape.

1. Square
2. Rectangle
3. Oval
4. Circle
5. Triangle pointing down
6. Triangle pointing left
7. Right triangle
8. Trapezoid
9. 6 Point star
10. Square Diamond
11. Pacman

### 2. Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

### 3. Find the single different character between two strings

Assume two strings str1, str2, where str2 contains the same set of characters in str1 with one additional character. Find the signal different character between the two strings.

Examples:

```
'abcd', 'abcde' -> 'e'
'aaabbcdd', 'abdbacade' -> 'e'
```