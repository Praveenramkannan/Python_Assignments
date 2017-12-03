'''
name:forbidden.py
date:2-12-20017
author:praveen.ram.kannan@accenture.com
question:Modify your program to prompt the user to enter a string of forbidden letters and then print the number of words that don’t contain any of them. Can you find a combination
 of 5 forbidden letters that excludes the smallest number of words?
'''
def avoids(word, forb):
    for letter in forb:
        if letter in word:
            return False
    return True

def no_contain(fin):
    forb = raw_input('enter the forbidden letters: ')
    count = 0
    for word in fin:
        if avoids(word, forb):
            count += 1
    return count

if __name__ == '__main__':
    fin = raw_input("Enter the words").split(" ")
    
    print no_contain(fin)
    print "no.of words are without forbidden letters"