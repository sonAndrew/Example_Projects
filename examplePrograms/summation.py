"""
    File: summation.py
    About: A function that add numbers together
"""
low = int(input("Enter lower number: "))
up = int(input("Enter upper number: "))

def summation(lower, upper):
    """
        Arguments: A lower bound and an upper bound
        Returns: The sum of the numbers from lower through upper
    """
    result = 0
    while lower <= upper:
        result += lower
        lower += 1
        print(result)
    return result
    

summation(low, up)