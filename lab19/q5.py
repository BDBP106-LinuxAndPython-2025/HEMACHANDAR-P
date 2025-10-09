#!/usr/bin/python3

# (5) Write a program to find the sum of all the elements in a list using lambda and reduce
# functions.

from functools import reduce

numbers = [1, 2, 3, 4, 5]
total_sum = reduce(lambda x, y: x + y, numbers)
print(f"Sum of all elements: {total_sum}")
