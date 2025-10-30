#!usr/bin/python3

# (5) You are given two 1D arrays. Write a function to create a new array that contains the
# maximum of the respective elements in the two arrays. For example, if a=[1,2] and
# b=[0,5] then the new array will be c=[1,5].
import numpy as np

a = np.array([11,2])
b = np.array([28,5])
c = np.maximum(a,b)

print("Element-wise maximum:", c)
