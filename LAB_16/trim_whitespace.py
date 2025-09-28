#!/usr/bin/python3

#(7) Write a script to trim leading whitespace characters from a string, S.

S=input("Enter the string: ")
start_index=0
for i in range(0,len(S)):
  if i == '':
      continue
  else:
      start_index=i
else:
    start_index=len(S)
trimmed = S[start_index:]
print(S)
