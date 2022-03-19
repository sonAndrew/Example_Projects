"""
    File: split.py
    About: Methods for Inserting, Changing, Adding and Removing Elements
"""
# Using split to change a list
print("Using split to change a list")
sentence = "This example has five words."

print(sentence)
print("-")

words = sentence.split()

print(words)
print("-")

# Using upper() function on all words in -words
print("Using upper() function on all words in -words")
for index in range(len(words)):
    words[index] = words[index].upper()

print(words)
print("-")
