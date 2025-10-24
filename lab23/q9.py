#!usr/bin/python3
# (9) Check for the presence of a BisI restriction site using regular expression character groups:
# A character group is a pair of square brackets with a list of characters inside them. dna
# = ”ATCGCGAATTCAC” pattern = GCNGC, where N represents any base, i.e. A, T,
# G, C

import re

dna = "ATCGCGAATTCAC"
pattern = r"GC[ATGC]GC"
if pattern in dna:
    print("Yes,the sequence matches the pattern")
else:
    print("No,the sequence does not match the pattern")
# print(bool(re.search(pattern, dna)))
