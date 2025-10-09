#!/usr/bin/python3

#(3) Write a program to convert a tuple of angles into a list of tuples with each tuple containing
# the sine and cosine of an angle

import math

angles = (0, math.pi/6, math.pi/4, math.pi/3, math.pi/2)#angle 0,30,45,60,90

# Using map to apply sine and cosine to each angle
result = list(map(lambda x: (math.sin(x), math.cos(x)), angles))

print(result)
