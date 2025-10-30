#!usr/bin/python3

# (6) Explore the set_print options() function to print a 3x3 matrix containing random
# numbers up to 3 decimal places.
import numpy as np
np.set_printoptions(precision=3)
mat = np.random.rand(3,3)
print("3x3 matrix with 3 decimals:\n", mat)
