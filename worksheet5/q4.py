#!/usr/bin/python3
#
# (4) Define a module called factorial that
# contains a function to calculate the factorial of a given integer.
# Using this function, find the permutation and combination of the given inputs.

# factorial.py
def factorial(n):
    """
    Calculate the factorial of a given number n.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def permutation(n, r):
    """
    Calculate permutation (nPr) using the formula: n! / (n-r)!
    """
    return factorial(n) // factorial(n-r)

def combination(n, r):
    """
    Calculate combination (nCr) using the formula: n! / (r! * (n-r)!)
    """
    return factorial(n) // (factorial(r) * factorial(n-r))


