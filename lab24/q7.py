#!/usr/bin/python3

# (7) Explore the set_printoptions() function to pretty-print a numpy array by suppressing
# the scientific notation (like 1e10).
import numpy as np
# print(help(np.set_printoptions))
arr = np.array([1.23e10, 2.34e11, 3.45e12, 0.00012345])
np.set_printoptions(suppress=False, precision=2)
print(arr)

