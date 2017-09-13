# 1 Uppercase a String
# Given a string, print the string uppercased.

string = 'lorem ipsum dolor sit amet, consectetur adipisicing elit.'

# print(string.upper())

# #############################################################################
# 2 Capitalize a String
# Given a string, print the string capitalized.

# print(string.capitalize())

# #############################################################################
# 3 Reverse a String
# Given a string, print the string reversed.

# print(" ".join(string.split(" ")[::-1]))

# #############################################################################
# 4 Leetspeak
# Given a paragraph of text as a string, print the paragraph in leetspeak.

# leetSpeak = {
#     'A': 4,
#     'E': 3,
#     'G': 6,
#     'I': 1,
#     'O': 0,
#     'S': 5,
#     'T': 7
# }

# for letter in leetSpeak:
#     string = string.upper().replace(letter, str(leetSpeak[letter]))
#
# print(string.lower())

# #############################################################################
# 5 Long-long Vowels
# Given a word as a string, print the result of extending any long vowels to the length of 5

# string = 'Good'
# count = {
#     'a': 0,
#     'e': 0,
#     'i': 0,
#     'o': 0,
#     'u': 0
# }
#
# for letter in string.lower():
#     if letter in count:
#         count[letter] += 1
#
# print(count)
# for letter in count:
#     if count[letter] >= 2:
#         string = string.replace(letter, letter*4, 1)
#
# print(string)

# #############################################################################
# 6 Caesar Cipher
# Given a string, print the Caesar Cipher (or ROT13) of that string.
# What is Caesar Cipher? http://practicalcryptography.com/ciphers/caesar-cipher/
# Use your solution to decipher the following text: "lbh zhfg hayrnea jung lbh unir yrnearq"

string = "lbh zhfg hayrnea jung lbh unir yrnearq"
strList = []

# 'z' == 122
for letter in string:
    if (ord(letter)) == 32:
        strList.append(chr(ord(letter)))
        continue
    if (ord(letter)+1) > 122:
        strList.append('a')
    else:
        strList.append(chr(ord(letter)+1))

print("".join(strList))
