#!/usr/bin/python3

#(8) Write a program to find the sum and average of numbers in a list, L.
L=input("input a list: ")
#L=[1,2,3,4,5,6,7,8,9]
L=L.split()
sum=0
average=0
L=[ int(L) for L in L ]
for i in L:
    sum=sum+i
    average=sum/len(L)

print(sum)
print(average)