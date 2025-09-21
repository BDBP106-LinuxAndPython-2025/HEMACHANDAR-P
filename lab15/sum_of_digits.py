#!/usr/bin/python3

#(6) Write a program to print the sum of the digits in a number.

a=(input("Enter a number: "))
sum=0
for i in a:
    sum=sum+int(i)
print(sum)
