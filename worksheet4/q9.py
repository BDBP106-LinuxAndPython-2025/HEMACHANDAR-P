#!/usr/bin/python3

#9. How to read a file’s contents one line at a time?
with open("IA1-sequence.txt", "r") as f:
    for line in f:
        print(line.strip())
