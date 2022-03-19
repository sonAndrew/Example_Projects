"""
    File: append.py
    About: appending and element
"""
print("- About: Appending and element")
example = [1, 2]
print(example)
print("-")

example.append(3)
print(example)
print("-")

# Extends the main list by adding a list
example.extend([11, 12, 13])
print(example)
print("-")

# Temporarily Adds the list to the main list
print(example + [14, 15])
print("-")

# Permanently Adds the list to the main list
example = example + [14, 15]
print(example)
print("-")

print(example)
print("-")

