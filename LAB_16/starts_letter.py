#!/usr/bin/python

#(15) Extract words from a list of strings L whose first character is k
L = ["kite", "king", "apple", "kangaroo", "banana", "key"]
k = 'k'

result = [word for word in L if word.startswith(k)]

print("Words starting with", k, ":", result)
