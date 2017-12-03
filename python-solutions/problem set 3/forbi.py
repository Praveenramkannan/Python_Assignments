'''
name:forbi.py
date:2-12-20017
author:praveen.ram.kannan@accenture.com
question:Write a function named avoids that takes a word and a string of forbidden letters, and that
 returns True if the word doesnt use any of the forbidden letters
'''
def avoids(word, forb):
    for letter in forb:
        if letter in word:
            return 0
    return 1


if __name__ == '__main__':
    fin = raw_input("Enter the words").split(" ")
    forb=['a','e','i','o','u']
    flag=avoids(fin,forb)
    if flag==0:
        print "False the given words contain forbidden letters."
    if flag==1:
        print "True, the given words doesnot contain forbidden letters"