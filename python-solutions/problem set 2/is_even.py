'''
name:is_even.py
date:2-12-20017
author:praveen.ram.kannan@accenture.com
question:Implement a function that satisfies the specification. Use a try-except block.
def findAnEven(l):
    """Assumes l is a list of integers
    Returns the first even number in l
    Raises ValueError if l does not contain an even number"""
'''
def is_even(s):
    for i in s:
        n=int(i)
        if(n%2==0):
            print n," is the first even number"
            break
        else:
            continue
    
    

n =raw_input("Enter the numbers").split(' ')
is_even(n)


