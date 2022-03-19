"""
    File: simpleList2.py
    About : Examples of using the range() function on list. 
    About : Also using len, [], +, and ==.
"""
# Imports
import math

first = [1, 2, 3, 4]
second = list(range(1, 5))

print(first)
print(second)

third = list("Hi there!")
print(third)

# len, [], +, and == work on lists as expected:
print(len(first))
print(first[0])
print(first[2:4])

# Concatentation (+) and equality (==) also work as expected for lists:
print(first + [5, 6])
print(first == second)