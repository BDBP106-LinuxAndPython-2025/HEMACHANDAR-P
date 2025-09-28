#!/usr/bin/pyhton3

#(5) Write a script to print the first half of a string, S.

S=input("Enter the string: ")
for i in range(0,len(S)//2):
    print(S[i])