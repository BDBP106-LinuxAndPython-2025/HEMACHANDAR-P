#!/usr/bin/python3

#(5) Write functions to add and subtract two matrices of m× n. Below these two functions,
#create two example matrices that have the same dimensions (rows and columns) and
#therefore correctly does the addition and subtraction Also come up with an example
#where the addition and subtraction are not defined, and hence the runtime errors show
#up.
A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

def add_matrices(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices must have the same dimensions to be added.")

    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        result.append(row)
    return result


def subtract_matrices(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Matrices must have the same dimensions to be subtracted.")

    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] - B[i][j])
        result.append(row)
    return result

# Addition
added = add_matrices(A, B)
print("A + B =", added)

# Subtraction
subtracted = subtract_matrices(A, B)
print("A - B =", subtracted)
