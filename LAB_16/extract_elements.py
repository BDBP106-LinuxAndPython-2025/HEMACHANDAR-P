#!/usr/bin/python3

#(13) Extract elements of a list if it occurs more than k times

L = [1, 2, 3, 2, 4, 2, 5, 3, 3]
k = 2

# Count occurrences
from collections import Counter
count = Counter(L)

# Extract elements occurring more than k times
result = [x for x in count if count[x] > k]

print("Elements occurring more than", k, "times:", result)
