#!/usr/bin/pyhton3

#(5) Write a script to print the first half of a string, S.

S=input("Enter the string: ")
i=0
for l in range(0,len(S),i+2):
    print(S[l])