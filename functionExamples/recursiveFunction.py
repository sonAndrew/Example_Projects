"""
    About: Summation function before turned into recursive function
"""
# def displayRange(lower, upper):
#     # Outputs the numbers from lower through upper.
#     while lower <= upper:
#         print(lower)
#         lower = lower + 1

"""
    About: Summation function after being turned into a recursive function
"""
# Get input and turn it into an integer
from unittest import result


low = int(input("Enter lower number: "))
up = int(input("Enter upper number: "))

def summation(lower, upper):
    # Returns the sum of the numbers from lower through upper.
    if lower > upper:
        return 0
    else:
        results = lower + summation(lower + 1, upper)
        print(results)
        return lower + summation(lower + 1, upper)