'''
name:largest_among_10.py
date:2-12-20017
author:praveen.ram.kannan@accenture.com
question:Write a program that asks the user to input 10 integers,
 and then prints the largest odd number that was entered. 
If no odd number was entered, it should print a message to that effect.
'''
largest = 0

for i in range(1, 11):
    number = int(raw_input('Enter integer %d: ' % i))
    if number % 2 != 0 and (number > largest):
        largest = number

if largest is None:
    print "You didn't enter any odd numbers"
else:
    print "Your largest odd number was:", largest