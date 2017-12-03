'''
name:newton_sqrt.py
date:2-12-20017
author:praveen.ram.kannan@accenture.com
question:Write a function NewtonSqrt() to abstract the Newton's Method of calculation Square roots.
'''

y = float(raw_input("Enter a number you want square rooted: ")) 

prevx = -1.0
x = 1.0
while abs(x - prevx) > 1e-10:  # Loop until x stabilizes
    prevx = x
    x = x - (x*x - y) / (2*x)
print(x)