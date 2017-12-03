'''
name:no_e_list.py
date:2-12-20017
author:praveen.ram.kannan@accenture.com
question: Modify the above program to print only the words that have no e 
and compute the percentage of the words in the list have no e
 '''

from __future__ import division
def has_no_e(word):
    for char in word:
        if char in 'Ee':
            return False
    return True  

count = 0
c=0
fin=(raw_input("Enter the words:")).split(' ')
print "The words with no 'e'"
for word in fin:
    c+=1
    if has_no_e(word):
        count += 1
        print word

percent = (count / c) * 100

print str(percent) + "% of the words don't have an 'e'."
