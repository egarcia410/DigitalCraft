# 1 Exercise 1

# phonebook_dict = {
#   'Alice': '703-493-1834',
#   'Bob': '857-384-1234',
#   'Elizabeth': '484-584-2923'
# }
#
# print(phonebook_dict['Elizabeth'])
# phonebook_dict['Kareem'] = '938-489-1234'
# del phonebook_dict['Alice']
# phonebook_dict['Bob'] = '968-345-2345'
# for key in phonebook_dict:
#     print(key, phonebook_dict[key])

# #############################################################################
# Exercise 2: Nested Dictionaries

# ramit = {
#   'name': 'Ramit',
#   'email': 'ramit@gmail.com',
#   'interests': ['movies', 'tennis'],
#   'friends': [
#     {
#       'name': 'Jasmine',
#       'email': 'jasmine@yahoo.com',
#       'interests': ['photography', 'tennis']
#     },
#     {
#       'name': 'Jan',
#       'email': 'jan@hotmail.com',
#       'interests': ['movies', 'tv']
#     }
#   ]
# }
#
# print(ramit['email'])
# print(ramit['interests'][0])
# print(ramit['friends'][0]['email'])
# print(ramit['friends'][1]['interests'][1])

# #############################################################################
# 3 Letter Summary

# def letter_histogram(word):
#     letterDict = {}
#
#     for letter in word:
#         if letter in letterDict:
#             letterDict[letter] += 1
#         else:
#             letterDict[letter] = 1
#     return letterDict
#
# word = 'banana'
# print(letter_histogram(word))

# #############################################################################
# 4 Word Summary

def word_histogram(words):
    wordDict = {}
    for word in words.split(" "):
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word] = 1
    return wordDict

words = 'One fish two fish red fish blue fish blue blue red'
# print(word_histogram(words))

# #############################################################################
# 5 Bonus Challenge
# Given a histogram tally (one returned from either letter_histogram or word_summary), print the top 3 words or letters.

def top3(words):
    wordDict = word_histogram(words)
    newList = sorted(wordDict, key=wordDict.get, reverse=True)
    return newList[:3]

print(top3(words))
