#!/usr/bin/python3

#(10) Write a program to find the even numbers in a list, L.

A=input("Enter the lsit of numbers you want to check: ")
B=A.split()
C=[int(x) for x in B]
for i in C:
    if i%2==0:
        print (i)

