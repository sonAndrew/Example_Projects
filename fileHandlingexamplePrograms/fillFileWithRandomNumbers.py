"""
    File   :  fillFileWithRandomNumber.py
    About  :  This program fills a file with 100 random integers in the range 1-500
"""
import random

f = open("integers.txt", 'w')
for count in range(100):
    number = random.randint(1, 500)
    f.write(str(number) + '\n')
f.close()
print("File filled")