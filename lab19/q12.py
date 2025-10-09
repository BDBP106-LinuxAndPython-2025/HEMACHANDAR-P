#!/usr/bin/python3

#(12) Write a program to extract all vowels in a given string using list comprehension.

vowels=['A','E','I','O','U','a','e','i','o','u']
a=input("Enter a sentence to analyse: ")

# c=[]
# for i in a:
#    if i in vowels:
#         c.append(i)
#         print(c)

# Using list comprehension to extract vowels
c = [i for i in a if i in vowels]

print("Vowels found:", c)
