#!/usr/bin/python3

#13)Write a program to print the factorial of a number

a=(input("enter the number: "))
fact=1
for i in range(1,int(a)+1):
    fact=fact*i
print ("factorial of ",i," is ",fact)