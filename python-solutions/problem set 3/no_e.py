'''
name:no_e.py
date:2-12-20017
author:praveen.ram.kannan@accenture.com
question:Write a function called has_no_e that returns
 True if the given word doesn’t have the letter "e" in it.
 '''
 
def check_e(str):
    for i in str:
        if(i=='e'):
            return 0
        else:
            return 1
                
str=raw_input("Enter a word")
a=check_e(str)
if(a==1):
    print " No E present in the word"
if(a==0):
    print"e is in given word"