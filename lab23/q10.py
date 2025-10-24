#!/usr/bin/python3
# (10) Take a DNA sequence and determine whether or not it contains any ambiguous bases –
# i.e. any bases that are not A, T, G or C. If there is a non ambiguous base, print the non
# ambiguous bases. dna = ”ATCGCGYAATTCAC”

import re

dna = "ATCGCGyuAATTCAC"
pattern = r"[^ATGC]"
if re.search(pattern, dna):
    print("Ambiguous base found!")
else:
    print("No ambiguous bases.")
