'''
name:volume_of_sphere.py
date:2-12-20017
author:praveen.ram.kannan@accenture.com
question:The volume of a sphere with radius r is 4/3pr3. What is the volume of a sphere with radius 5?
Hint: 392.7 is wrong!
'''
from __future__ import division
def volume(r):
    volume=4/3*3.14*r*r*r
    print "the volume of the sphere is :%f" %volume
    

radius=int(raw_input("enter the radius of the sphere"))
volume(radius)