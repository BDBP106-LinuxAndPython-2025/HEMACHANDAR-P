#!/usr/bin/python3

#(5) Write a script to find the first occurrence of a character, c, in a string S.

S=(input("Enter a sentence: "))

for i in range(len(S)):
    if S[i]=='c':
        break
print (i)


