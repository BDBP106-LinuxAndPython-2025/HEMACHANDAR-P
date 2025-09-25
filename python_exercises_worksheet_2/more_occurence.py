#!/usr/bin/python3

#(6) Write a script to find the highest frequency character in a string, S.

S=input("enter a string: ")
max_char=''
max_count=0

for i in S:
    count = 0
    for c in S:
        if i==c:
            count=count+1
        if count>max_count:
            max_count=count
            max_char=i
print("max char is",max_char)
print("max count is",max_count)