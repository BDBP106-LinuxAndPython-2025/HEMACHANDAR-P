#!/usr/bin/python3

import re

dna_seq = "ACTGCATTATATCGTACGAAAATTATACGCGCG"
pattern = r"TATACGCGCG"

matches = re.findall(pattern, dna_seq)
print("Matched part(s):", matches)
