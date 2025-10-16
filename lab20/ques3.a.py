#!/usr/bin/pyython3
# (a) Create a simple text file containing the following string matrix, and save it as
# ‘stringmatrix.dat’. This should be saved as a separate program called ”Q3 a.py”.
# (Hint: For those aware of ascii values for alphabets and know how to use them, the
# ascii value of ‘A’ is 65, and one can get the alphabet string by calling chr(65).)
# A B C D
# E F G H
# I J K L
matrix = [['A', 'B', 'C', 'D'],['E', 'F', 'G', 'H'],['I', 'J', 'K', 'L']]
# Opening the file in write mode
with open('stringmatrix.dat', 'w') as file:
    for i in matrix:
        # Join the row elements by space and write to the file
        file.write(' '.join(i) + '\n')
