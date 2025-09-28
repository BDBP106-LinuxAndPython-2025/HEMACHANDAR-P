#!/usr/bin/python3

#(8) Write a script to count the number of occurrences of a word, W, in a sentence, S.

S=input("Enter a sentence: ")
W=input("Enter a word to find: ")
words=S.split()

count=0
for i in words:
    if i==W:
        count=count+1
print(count)




