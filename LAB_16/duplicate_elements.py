#!usr/bin/python3

#(11) Write a program to print the duplicate elements in a list, L.

A=input("Enter the list of numbers: ")
B=A.split()
C=[int(x) for x in B]
D=sorted(C)
duplicates = set()
for i in range(0,len(D)-1):
    if D[i]==D[i+1]:
        duplicates.add(D[i])

if duplicates:
    print("Duplicate elements:", duplicates)
else:
    print("No duplicates found.")