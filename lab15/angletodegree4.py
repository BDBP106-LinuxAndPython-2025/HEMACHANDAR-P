#!/usr/bin/python3

#Write a python script to take an input angle in degrees and print the values of all the 6
#trigonometric functions for this angle. Remember to write a line of code to convert your
#input into radians before finding the trigonometric values.

import math
a=float(input("Enter the angle: "))

b=(a*math.pi/180)

c=math.sin(b)
d=math.cos(b)
e=math.tan(b)
f=(1/math.sin(b))
g=(1/math.cos(b))
h=(1/math.tan(b))

print(c,d,e,f,g,h)