def pythTriple():
    # Ensure a < c
    for c in range(2, 1000):
        for a in range(1, c):
            # Ensure a + b + c == 1000.  Since a is counting up, the first
            # answer we find should have a <= b.
            b = 1000 - c - a

            # Ensure Pythagorean triple
            if a**2 + b**2 == c**2:
                print("a = {}, b = {}, c = {}  abc = {}".format(a, b, c, a * b * c))
                return
pythTriple()

def singleDiff(str1, str2):
    for letter in str2:
        if letter not in str1:
            return letter


str1 = 'aaabbcdd'
str2 = 'abdbacade'
print(singleDiff(str1, str2))