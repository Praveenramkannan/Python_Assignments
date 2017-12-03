'''
name:books.py
date:2-12-20017
author:praveen.ram.kannan@accenture.com
question:Observe the Code Snippet
a. What would the  
code above return if the statement x = 25 were replaced by x = -25?
'''
x = 25 #if x=-25, an infinite loop runs
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon:
    print 'low =', low, 'high =', high, 'ans =', ans
    numGuesses += 1
    if ans**3 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/8.0
print 'numGuesses =', numGuesses
print ans, 'is close to square root of', x