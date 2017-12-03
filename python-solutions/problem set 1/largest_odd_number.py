'''
name:largest_odd_number.py
date:2-12-20017
author:praveen.ram.kannan@accenture.com
question:Write a program that examines three variables—x, y, and z— 
and prints the largest odd number among them.
 If none of them are odd, it should print a message to that effect.
'''
num1=int(raw_input("Enter the first number"))
num2=int(raw_input("Enter the second number"))
num3=int(raw_input("Enter the third number"))
if num1%2!=0 and num2%2!=0 and num3%2!=0:
    print "all the numbers are odd nuumbers"
    if num1>num2 and num1>num3:
        print "num1 is largest"
    elif num2>num1 and num2>num3:
        print "num2 is largest" 
    else:
        print "num3 is largest"
elif num1%2!=0 and num2%2!=0 and num3%2==0 :
    print "num1,num2 are odd and num 3 is even"
    if(num1>num2):
        print("among num1 and num2, num 1 is largest")
    else:
        print("among num1 and num2, num 2 is largest")
elif num1%2!=0 and num2%2==0 and num3%2==0 :
    print "num1 is the largest"
elif num1%2==0 and num2%2!=0 and num3%2!=0 :
    print "num3,num2 are odd and num 1 is even"
    if(num2>num3):
        print("among num2 and num3, num 2 is largest")
    else:
        print("among num1 and num2, num 3 is largest")
elif num1%2==0 and num2%2!=0 and num3%2==0 :
    print "num2 is the largest"
elif num1%2!=0 and num2%2==0 and num3%2!=0 :
    print "num1,num3 are odd and num 2 is even"
    if(num1>num3):
        print("among num1 and num3, num 1 is largest")
    else:
        print("among num1 and num3, num 3 is largest")
elif num1%2==0 and num2%2==0 and num3%2!=0 :
    print "num3 is the largest"
else:
    print "No nos are odd"
    

    