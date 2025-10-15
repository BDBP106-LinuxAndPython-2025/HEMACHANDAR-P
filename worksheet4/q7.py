#!/usr/bin/python3

# 7. How to confirm if a file has been closed or not:

f = open("IA1-sequence.txt", "r")
print(f.closed)  
f.close()
print(f.closed)
