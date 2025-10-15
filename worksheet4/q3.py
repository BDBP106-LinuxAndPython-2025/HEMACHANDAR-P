#!/usr/bin/python3

# (3) Write a list comprehension to create a list of names that start with ‘’H’ or ‘ase; in a
# given list of protein names. For example,
#proteins=["Hexokinase", "Amylase","Hemoglobin", "Catalase", "Actin"]
proteins = ["Hexokinase", "Amylase", "Hemoglobin", "Catalase", "Actin"]
filtered_names = [p for p in proteins if p.startswith('H') or p.endswith('ase')]
print(filtered_names)
# Output: ['Hexokinase', 'Amylase', 'Hemoglobin', 'Catalase']
