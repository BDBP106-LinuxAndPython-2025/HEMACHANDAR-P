#!/usr/bin/python3

# (2) Write a list comprehension to output the AT content in % in a list of DNA sequences.
# For example, sequences=["ATGC", "GGCC","AATT","GCGC"]
sequences = ["ATGC", "GGCC", "AATT", "GCGC"]
at_content = [((sequence.count('A') + sequence.count('T')) / len(sequence)) * 100 for sequence in sequences]
print(at_content)  # Output: [50.0, 0.0, 100.0, 0.0]
