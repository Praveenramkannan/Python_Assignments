'''
name:sum_of_nos.py
date:2-12-20017
author:praveen.ram.kannan@accenture.com
question:Implement a function that meets the specification below. Use a try-except block.

def sumDigits(s):
    """Assumes s is a string
    Returns the sum of the decimal digits in s
    For example, if s is 'a2b3c' it returns 5"""
'''
def noadd(s):
    sum=0
    for i in s :
            try:
                if i in['0','1','2','3','4','5','6','7','8','9']:
                    i=int(i)
                    sum=sum+i
            except:
                print "Exception"
    print "The sum is ",sum
s=raw_input("Enter the string")
noadd(s)