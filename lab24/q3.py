#!/usr/bin/python3
# (3) We know how to reverse the elements in a 1D array- a[::-1]. How would you reverse
# the rows in a 2D array? How would you reverse the columns in a 2D array?
import numpy as np

# Create a 3x3 array with random integers from 1 to 100
arr = np.random.randint(1,100, (4,5))
print("Original array:\n", arr)

# Reverse rows
rows_reversed = arr[::-1, :]
print("Rows reversed:\n", rows_reversed)

# Reverse columns
cols_reversed = arr[:, ::-1]
print("Columns reversed:\n", cols_reversed)

