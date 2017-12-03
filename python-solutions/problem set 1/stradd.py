'''

name:stradd.py
date:2-12-20017
author:praveen.ram.kannan@accenture.com
question:Let s be a string that contains a sequence of decimal numbers 
separated by commas, e.g., s = '1.23,2.4,3.123'. 
Write a program that prints the sum of the numbers in s.
'''

str=raw_input("enter comma separated decimal numbers")
lis=str.split(",")
print lis
n=0.0
for i in lis:
    n=n+float(i)
print "The sum of decimal values is :",n