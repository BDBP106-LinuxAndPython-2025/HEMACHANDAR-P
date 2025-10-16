#!/usr/bin/python3
# (b) Next, in a new program, read in the matrix of strings in the above file as a 2D array
# of list of lists. The number of rows and columns are not known in advance. Make
# sure your code can figure out how many rows and columns are there in this input.
# Name this list as grid and print this 2D list. Name this program as ”Q3 b.py”. In
# this same program, print a list that contains lists of columns of the above matrix.
# For example, the first column will be grouped into a list [A,E,I] and so on. Next,
# print a list that prints the diagonal elements read in one direction. For example,
# some of the elements in this list will be [‘A’],[‘B’,‘E’],[’C’,‘F’,‘I’] and so on.

# Read the file and build the 2D list grid
with open('stringmatrix.dat', 'r') as file:
    lines = file.readlines()

# Strip newlines and split each line by spaces to create the grid
grid = [line.strip().split() for line in lines]
print(grid)
print()
print(grid[0])
print()
print(grid[1])
print()
print(grid[2])
print()

# Number of rows and columns
rows = len(grid)
print(f'{rows} rows')
print()
cols = len(grid[0])
print(f'{cols} columns')
print()

print("Grid (2D list):")
for row in grid:
    print(row)
print()
# Create a list of columns
columns = []
for c in range(cols):
    col = [grid[r][c] for r in range(rows)]
    print(col)
    columns.append(col)

print("\nColumns:")
for col in columns:
    print(col)

diagonals = []
for diag_sum in range(rows + cols - 1):
    diagonal = []
    # Loop through possible rows for this diagonal
    for r in range(rows):
        c = diag_sum - r
        if 0 <= c < cols:
            diagonal.append(grid[r][c])
    diagonals.append(diagonal)

print("\nDiagonals (top-right to bottom-left):")
for d in diagonals:
    print(d)
