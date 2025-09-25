#!/usr/bin/python3

#(7) Write a script to replace all occurrences of a character, c, with another character, d.

A=input("Give a string: ")
B=input("Give which letter to replace: ")
C=input("Give the letter(which to replace) to replace: ")
new_string=""
for i in A:
    if i==B:
        new_string=new_string+C
    else:
        new_string=new_string+i
print(new_string)

