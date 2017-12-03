'''
name:stropr.py
date:2-12-20017
author:praveen.ram.kannan@accenture.com
question:Write a function isIn() that accepts two strings as 
arguments and returns True if either string occurs 
anywhere in the other, and False otherwise.
 Hint: you might want to use the built-in str operation in.
'''
def str_match(s1,s2):
    if str1 in str2 or str2 in str1:
        print "Strings match"
    else :
        print "No match found"
str1=raw_input("Enter the first string")
str2=raw_input("Enter the second string")
str_match(str1,str2)
