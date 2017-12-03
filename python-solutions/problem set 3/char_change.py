'''
name:char_change.py
date:2-12-20017
author:praveen.ram.kannan@accenture.com
question:Write a function called rotate_word() that takes a string and an integer as parameters, and that returns a new string that contains 
the letters from the original string "rotated" by the given amount
'''
def str_rotate(str,n):
    j=''
    for i in str:
        j=j+chr(ord(i) + n)
    print j     

str=raw_input("Enter the string:")
n=int(raw_input("Enter the no.of characters to be rotated"))
str_rotate(str,n)

