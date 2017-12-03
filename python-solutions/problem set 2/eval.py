'''
name:eval.py
date:2-12-20017
author:praveen.ram.kannan@accenture.com
question:Write a function called eval_loop that iteratively
 prompts the user, takes the resulting input and evaluates 
 it using eval, and prints the result. It should continue until the user enters 'done', 
and then return the value of the last expression it evaluated.
'''
import math
def eval_loop(s):
    ev=eval('%s' % s)
   # result=result+ev
    print ev
    a=raw_input("Want another eval? or done?")
    if(a=='done'):
        print "The last result is ",result
    else:
        eval_loop(a)


e=raw_input("Enter the expression:")
result=0    
eval_loop(e)