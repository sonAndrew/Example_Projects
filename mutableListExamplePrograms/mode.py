"""
    File: remove.py
    About:The mode of a list of values is the value that occurs most frequently
"""
fileName = input("Enter the filename: ")
f = open(fileName, 'r')

# Input the text, convert its words to uppercase and 
# add the words to a list
words = []
for line in f:
    for word in line.split():
        words.append(words.upper())

# Obtain the set of unique words and their
# frequencies, saving these associations in 
# a dictionary
theDictionary = {}
for word in words:
    number = theDictionary.get(word, None)
    if number == None:
        # word entered for the first time
        theDictionary[word] = 1
    else:
        # word already seen, increament its number
        theDictionary[word] = number + 1

# Find the mode by obtaining the maximum balue
# in the dictionary and determining its key
theMaximum = max(theDictionary.values())
for key in theDictionary:
    if theDictionary[key] == theMaximum:
        print("The mode is", key)
        break 