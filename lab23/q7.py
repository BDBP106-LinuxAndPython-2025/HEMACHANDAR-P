#!/usr/bin/python3
# (7) Test if a DNA sequence contains an EcoRI restriction site using regular expressions. dna
# = ”ATCGCGAATTCAC” pattern = GAATTC

import re

dna = "ATCGCGAATTCAC"
pattern = r"GAATTC"
if pattern in dna:
    print("Yes,the sequence matches the pattern")
else:
    print("No,the sequence does not match the pattern")
# print(bool(re.search(pattern, dna)))
