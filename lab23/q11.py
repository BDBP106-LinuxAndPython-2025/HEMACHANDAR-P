#!/usr/bin/python
# (11) Write a regular expression to split the DNA string wherever we see a base that isn’t A,
# T, G or C. if the dna = ”ACTNGCATRGCTACGTYACGATSCGAWTCG”, the output
# should be [’ACT’, ’GCAT’, ’GCTACGT’, ’ACGAT’, ’CGA’, ’TCG’]

import re

dna = "ACTNGCATRGCTACGATSCGAWTCG"
parts = re.split(r'[^ATGC]+', dna)
print(parts)
