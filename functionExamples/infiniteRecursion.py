"""
    About: An Infinite recursion arises when the coder 
            fails to specify base case or to reduce the 
            size of problem in a way that terminates 
            the recursive process.
"""

def runForever(n):
    if n > 0:
        runForever(n)
    else:
        runForever(n - 1)

# runForever(1)