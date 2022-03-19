"""
    File   :  binarytodecimal.py
    About  :  Turning a binary input to a decimal
"""
# Introduction to program.
bitString = input("Enter a string of bits: ")       # Get user input

# Variables
decimal = 0                                         # Set decimal variable to zero
exponent = len(bitString) - 1                       # Get the value of user input

# Change the binary value to decimal
for digit in bitString:                             # For each digit in the (user entered value)
    decimal = decimal + int(digit) * 2 ** exponent  # Get the actual decimal value
    exponent = exponent - 1                         # Subtract the length of the binary by 1

print("The integer value is", decimal)              # Print "The integer value is, " the final decimal value