'''
name:right_justify.py
date:2-12-20017
author:praveen.ram.kannan@accenture.com
question:Python provides a built-in function called len that returns 
the length of a string, so the value of len('Cigna') is 5. 
Write a function named right_justify that takes a string
 named s as a parameter and prints the string with enough leading spaces 
so that the last letter of the string is in column 70 of the display.
'''
def right_justify(s):
    print "%70s" % s
    
str=raw_input("Enter the string")
right_justify(str)