first = [20, 30, 40]
second = first

# Creating a list and making it equal to the list named first
third = list(first) # Or use first[:]

print(first == second)

print(first == third)

print(first is second)

print(first is third)

