"""
    File   :  sumNumbersInFile.py
    About  :  Compute the sum of the numbers in the file integers.txt
"""

f = open("integers.txt", 'r')
theSum = 0
for line in f:
    wordList = line.split()
    for word in wordList:
        number = int(word)
        theSum += number
print("The sum is", theSum)