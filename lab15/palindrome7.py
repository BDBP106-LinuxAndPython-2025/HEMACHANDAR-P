#!/usr/bin/python3
#(12) Write a program to check if an input string is palindrome
a = str(input("Enter a: "))
b = a[::-1]
if a == b:
    print ("palindrome")
else:
    print ("Not a palindrome")
