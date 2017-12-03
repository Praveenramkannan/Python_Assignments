'''
name:is_pal.py
date:2-12-20017
author:praveen.ram.kannan@accenture.com
question:A step size of -1 goes through the word backwards, so the slice [::-1] generates a reversed string. 
Use this idiom to write a one-line version of is_palindrome
'''
def is_pal(str):
    return str == str[::-1]
str=raw_input("Enter the string")
print(is_pal(str))
