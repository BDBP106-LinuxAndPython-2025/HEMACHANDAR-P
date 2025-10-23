#!usr/bin/python3
#
# (3) Implement matrix multiplication of matrices A and B without using any external packages
# as an instance method in a class called Linear Algebra. Get the no. of rows and
# columns and elements of each matrix from the user. Raise errors in case the condition
# for matrix multiplication is not met. Once you have a working code for this, decorate a
# function that returns the matrices A and B using @property. Then also define a setter
# function to allow the modification of A and B, since the user may make mistakes in
# inputting the matrices and should be able to change elements as desired. Lastly, define
# a custom decorator for calculating time in multiplying matrices A and B of size 50x50.

import time


def time_matrix_multiplication(func):
    """Custom decorator to time matrix multiplication"""

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Matrix multiplication took {end - start:.6f} seconds")
        return result
    return wrapper


class LinearAlgebra:
    def __init__(self, A, B):
        self.A = A
        self.B = B

    @property
    def matrices(self):
        return self.A, self.B

    @matrices.setter
    def matrices(self, matrices):
        A, B = matrices
        self.A = A
        self.B = B

    @time_matrix_multiplication
    def multiply(self):
        # Check multiplication condition
        if len(self.A[0]) != len(self.B):
            raise ValueError("Matrix multiplication condition not satisfied!")

        result = [[0 for _ in range(len(self.B[0]))] for _ in range(len(self.A))]
        for i in range(len(self.A)):
            for j in range(len(self.B[0])):
                for k in range(len(self.B)):
                    result[i][j] += self.A[i][k] * self.B[k][j]
        return result


# Example usage
A = [[1, 2, 3], [4, 5, 6]]
B = [[1, 4], [2, 5], [3, 6]]

la = LinearAlgebra(A, B)
C = la.multiply()

print("Resultant Matrix:")
for row in C:
    print(row)
