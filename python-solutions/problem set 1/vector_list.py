'''
name:vector_list.py
date:2-12-20017
author:praveen.ram.kannan@accenture.com
question:Implement a function that satisfies the specification. 
Use a try-except block.
'''

def getRatios(vect1, vect2):
    for i in vect1,vect2:
        try:
            print "The ratio is:",vect1/vect2
        except :
            print "Exception occured"
            
vect1=raw_input("Enter the first list").split(" ")
vect2=raw_input("Enter the second list").split(" ")
getRatios(vect1, vect2)