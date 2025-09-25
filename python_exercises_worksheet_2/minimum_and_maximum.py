#!usr/bin/python3

#(9) Write a program to find the minimum and maximum number in a list, L.

A=input("enter the list: ")

A=A.split()
A=[int(i) for i in A]
max=A[0]
min=A[0]

for i in A:
    if i>max:
        max=i
    elif i<min:
        min=i
print("maximum: ",max)
print("minimum: ",min)