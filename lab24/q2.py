#!/usr/bin/python3
# (2) Array creation and manipulation exercises. Print all the arrays in each exercise.
# (i) Create a 1D array from 0 to 9.
import numpy as np
array=np.arange(10)
print(f'array: {array}')
print()

# (ii) Create a boolean array of size 3x3.
boolean_arr = np.random.choice([True, False], size=(3,3))
print(f'boolean_arr: {boolean_arr}')
print()

# (iii) Using syntax from list comprehension, create an array that satisfies the condition.
# For example,
# arr = np.arange(10)
# arr = arr[ arr%2 == 1 ]
# Create an array of prime numbers from 1 to 50 using a similar approach.
prime_number = np.array([x for x in range(2, 51) if all(x % i != 0 for i in range(2, int(x**0.5)+1))])
print(f'prime_number:', prime_number)
print()
print()

# (iv) Create a 1D array with 20 random elements, and reshape it as a 4x5 array. Print
# the two arrays.
random_arr = np.random.randint(0, 100, 20)
rand_arr_reshaped = random_arr.reshape(4,5)
print("1D array:", random_arr)
print("Reshaped 4x5 array:\n", rand_arr_reshaped)
print()

# (v) Create two 1D arrays a and b where a has numbers ranging from 0 to 9 and b has
# only 1s. Then stack the two arrays horizontally.
a = np.arange(10)
b = np.ones(10, dtype=int)
horizontal_stack = np.hstack((a, b))
print(f'horizontal_stack:', horizontal_stack)
print()
print()

# (vi) Define two 1D arrays, where array a has list of first 100 numbers, and b has first
# 100 prime numbers. Obtain a new array that is the intersection of these two
# arrays (Hint: use np.intersect1d())
A=np.arange(1,101)
prime_number1= np.array([x for x in range(2,101) if all(x % i != 0 for i in range(2, int(x**0.5)+1))])
intersection=np.intersect1d(A,prime_number1)
# print(A)
print(f'intersection:',intersection)
print()

# (vii) Use the above two arrays with the aim this time to remove items from a that are
# in b. (We are doing a-b operation, use np.setdiff1d())
C=np.setdiff1d(A,intersection)
print(f'a-b:',C)
print()

# (viii) Use the above two arrays with the aim of getting the indices of common elements
# between the two arrays. (Hint: Use np.where(a==b))
# D=np.where(A == intersection)
indices_in_A = np.where(np.isin(A, intersection))[0]
print("Indices of common elements in A:", indices_in_A)
print()

# (ix) Extract the elements of the array a above that are greater than 5 and less than
# 20.
subset = A[(A > 5) & (A < 20)]
print(f'subset:',subset)



