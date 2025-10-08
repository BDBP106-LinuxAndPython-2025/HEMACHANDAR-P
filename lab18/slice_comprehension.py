#!/usr/bin/python3

#(1) List slicing examples We saw that in list splicing, if a is a list containing n = len(a) elements, then
# the slicing can be done with positive or negative steps a[start : stop : step]. By default, the step is
# 1 (so positive). For positive step values start = 0 and stop = n by default. If the step is negative,
# then the list is read from right to left, and start = −1 and stop = −n − 1 by default.
# In other words, Python checks whether the step is positive or negative
# (so that it knows what direction to iterate) and then checks whether start > stop for step < 0
# and start < stop for step > 0. If start = stop, then Python returns an empty list regardless of the step value.
# Let’s do some exercises with a list containing numbers 1 to 50. In each case, predict the result and
# cross-check with the result from Python. Also indicate what the respective start, stop and step values
# are in each case.

#(i) Create a list spanning 1 to 50 using list comprehension method. Call this list a.
a = [i for i in range(1, 51)]
print(a)

#(ii) Slicing with positive step:
a1=a[1:5]
print(a1)
#[2, 3, 4, 5]

a2=a[3:20:2]
print(a2)
#[4, 6, 8, 10, 12, 14, 16, 18, 20]

a3=a[::2]
print(a3)
#[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]

a4=a[::]
print(a4)
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]

a5=a[10::2]
print(a5)
#[11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]

a6=a[1:1:1]
print(a6)
#[]

a7=a[:0:]
#start = 0 (default), stop = 0, step = 1 (default)
#Since start == stop, output is empty list
print(a7)
#[]

a8=a[-7::1]
# Is the output a non-empty list? Why did this work?
print(a8)
#[44, 45, 46, 47, 48, 49, 50]

a9=a[-6:]
print(a9)
#[45, 46, 47, 48, 49, 50]

a10=a[-10:-4]
print(a10)
#[41, 42, 43, 44, 45, 46]

# (iii) Slicing with negative step:

a11 = a[::-1]
# start = -1 (last element), stop = -len(a)-1 = -51, step = -1 (reverse whole list)
print(a11)
# Output: [50, 49, 48, ..., 1]

a12 = a[::-3]
# start = -1, stop = -51, step = -3 (every 3rd element from end to start)
print(a12)
# Output: [50, 47, 44, 41, 38, 35, 32, 29, 26, 23, 20, 17, 14, 11, 8, 5, 2]

a13 = a[:1:-2]
# start = -1 (default for negative step), stop = 1, step = -2
# From last element backward to index 2 (stop exclusive), step -2
print(a13)
# Output: [50, 48, 46, ..., 4]

a14 = a[-1:-1:-1]
# start = -1, stop = -1, step = -1
# start == stop → empty list
print(a14)
# Output: []

a15 = a[:-5:-1]
# start = -1 (last element), stop = -5 (index 45), step = -1
# Elements from last to index 46 (exclusive) stepping backwards
print(a15)
# Output: [50, 49, 48, 47]

a16 = a[:0:-1]
# start = -1, stop = 0, step = -1
# From last element backward to index 1 (0 exclusive)
print(a16)
# Output: [50, 49, 48, ..., 2]

a17 = a[:-1:-1]
# start = -1, stop = -1, step = -1
# start == stop → empty list
print(a17)
# Output: []

a18 = a[0:-5:-1]
# start = 0, stop = -5 (index 45), step = -1
# Since step is negative but start < stop, no elements satisfy condition → empty
print(a18)
# Output: []

a19 = a[-1:5:-1]
# start = -1 (index 49), stop = 5, step = -1
# From last element backward to index 6 (exclusive)
print(a19)
# Output: [50, 49, 48, ..., 7]

a20 = a[2:2:-1]
# start = 2, stop = 2, step = -1
# start == stop → empty list
print(a20)
# Output: []

a21 = a[2:1:-1]
# start = 2, stop = 1, step = -1
# Start > stop and step < 0 → single element at index 2
print(a21)
# Output: [3]

a22 = a[0:-5]
# start = 0, stop = -5 (index 45), step = 1 (default)
# Elements from index 0 to 44 (inclusive of 0, exclusive of 45)
print(a22)
# Output: [1, 2, ..., 45]

# (iv) Modification of lists using list slicing:

# (a) Create a list of even numbers from 'a' using slicing:
evens = a[1::2]
# start = 1 (index of 2), stop = end, step = 2 (every second element starting at 2)
print(evens)
# Output: [2, 4, 6, 8, ..., 50]


