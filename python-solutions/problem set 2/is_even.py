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
def is_palindrome(s):
    s = s.lower()
    rev_str = reversed(s)
    if list(s) == list(rev_str):
        print("It is palindrome")
    else:
        print("It is not palindrome")

my_str = raw_input("Enter the string")
is_palindrome(my_str)


