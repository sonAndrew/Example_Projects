"""
    File: alias.py
    About: Aliases
"""
first = [10, 20, 30]
second = first
print(first)
print("-")

print(second)
print("-")

first[1] = 99
print(first)
print("-")

print(second)
print("-")

third = []
for element in first:
    third.append(element)

print(first)
print("-")

print(third)
print("-")

first[1] = 100
print(first)
print("-")

print(third)
print("-")