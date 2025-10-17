#!/usr/bin/python3

#12. Python script that lists each line of a file with its line number:

filename = "Heart.csv"

with open(filename, "r") as f:
    for i, line in enumerate(f, start=1):
        print(f"{i}: {line.strip()}")
