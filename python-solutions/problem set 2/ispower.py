'''
name:ispower.py
date:2-12-20017
author:praveen.ram.kannan@accenture.com
question:A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a function called is_power that takes parameters a and b and returns True if a is a power of b.
 Note: you will have to think about the base case.
'''
def is_power(a,b):
    if(a%b != 0):
        return False
    elif(a/b == 1):
        return True
    else:
        return is_power(a/b,b)
a=int(raw_input("Enter the value of a :"))
b=int(raw_input("Enter the value of b :"))
c=is_power(a, b)

if(c==True):
    print "True"
else:
    print "False"