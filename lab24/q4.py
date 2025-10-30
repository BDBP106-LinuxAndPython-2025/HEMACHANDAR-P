#!/usr/bin/python3

# (4) Thinking along the same lines of the above question, how will you swap two columns in
# a 2D array? Define a 3x3 matrix with random values, and swap first and second columns
# in this array.
# Define a 3x3 random matrix
import numpy as np
matrix = np.random.randint(1, 100, (3,3))
print("Original matrix:\n", matrix)

# Swap first and second columns
matrix[:, [0, 1]] = matrix[:, [1, 0]]
print("After swapping first and second columns:\n", matrix)

