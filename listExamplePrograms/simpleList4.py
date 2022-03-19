"""
    File  : simpleList4.py
    About : Examples of the mutablity of list.
"""
# Example List
print("Example List")
example = [1, 2, 3, 4]
print(example)
print("-")

# Change a certain index
print("Change a certain index")
example[3] = 0

print(example)
print("-")

# Example List
print("Example List")
numbers = [2, 3, 4, 5]

print(numbers)
print("-")

# Using change the index within a range
print("Using change the index within a range")
for index in range(len(numbers)):
    numbers[index] = numbers[index] ** 2

print(numbers)
print("-")

