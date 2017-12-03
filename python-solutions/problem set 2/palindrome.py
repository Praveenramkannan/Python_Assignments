'''
name:palindrome.py
date:2-12-20017
author:praveen.ram.kannan@accenture.com
question:Ensure you build a test function testIsPalindrome() that tests your palindrome function.
'''
def pal(str):  
    rev_str=reversed(str)
    if(list(str)==list(rev_str)):
        print "It is a palindrome"
    else:
        print "It is not a palindrome"

str=raw_input("Enter a string")
pal(str)