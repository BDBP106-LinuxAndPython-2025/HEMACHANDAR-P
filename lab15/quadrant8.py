#!/usr/bin/python3

#(8) Write a program to tell which quadrant a given point lies in the first, second, third or
#fourth quadrant

a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
if a==0 and b==0:
    print("The number is the origin")
else:
    if (a>=0 and b>=0):
        print("The number is in quadrant 1")
    elif (a<=0 and b>=0):
        print("The number is in quadrant 2")
    elif (a<=0 and b<=0):
        print("The number is in quadrant 3")
    else:
        print("The number is in quadrant 4")
