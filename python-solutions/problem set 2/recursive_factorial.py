'''
name:recursive_fact.py
date:2-12-20017
author:praveen.ram.kannan@accenture.com
question:Observe the following function definitions. They Calculate the Factorial as per the Mathematical definition 1! = 1 (n + 1)! = (n + 1) * n! Implement factI(n) as an recursive Implementation
'''
def fact(n):
	if(n>1):
		return n*fact(n-1)
	if(n==1):
		return 1
print "Program to find factorial"
n=int(raw_input("Enter the number:"))
factorial=fact(n)
print "The factorial is :",factorial