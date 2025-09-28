#!/usr/bin/python3

#(9) Write a script to check if two strings are anagrams of each other . listen and silent
#are anagrams, gram and arm are not anagrams

A=input("Enter the word you want to check: ")
B=input("Enter the word you want to check: ")
C=sorted(A.lower())
D=sorted(B.lower())

if C==D:
    print("The words are anagram")
else:
    print("The words are not anagram")