"""
    File   :  readFile.py
    About  :  Read text from a file.
"""

# Example 1
# f = open("inputFile.txt", 'r')

# text = f.read()
# text
# print(text)

# Example 2
f = open("inputFile.txt", 'r')
for line in f:
    print(line)
    
# Example 3
# f = open("inputFile.txt", 'r')
# while True:
#     line = f.readline()
#     if line == "":
#         break
#     print(line)

# Example 4
# f = open("integers.txt", 'r')
# theSum = 0
# for line in f:
#     line = line.strip()
#     number = int(line)
#     theSum += number
#     print("The sum is", theSum)