#!/usr/bin/pyhton3
# (8) Check for the presence of an AvaII recognition site, which can have two different se-
# quences: GGACC and GGTCC. Use regular expressions. dna = ”ATCGCGAATTCAC”
# pattern = GGACC and GGTCC

import re

dna = "ATCGCGAATTCAC"
pattern = r"(GGACC|GGTCC)"
if pattern in dna:
    print("Yes,the sequence matches the pattern")
else:
    print("No,the sequence does not match the pattern")
# print(bool(re.search(pattern, dna)))
