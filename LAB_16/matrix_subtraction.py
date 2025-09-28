#!/usr/bin/python3

rows = int(input("Enter the number of rows: "))
column = int(input("Enter the number of columns: "))

def input_matrix(rows, column):
    matrix = []
    for i in range(rows):
        row_input = input('Enter row with numbers separated by space: ')
        row = row_input.split()
        row = [int(num) for num in row]
        matrix.append(row)
    return matrix

print("Enter Matrix 1:")
m1 = input_matrix(rows, column)

print("Enter Matrix 2:")
m2 = input_matrix(rows, column)

result = []
for i in range(rows):
    row = []
    for j in range(column):
        row.append(m1[i][j] - m2[i][j])
    result.append(row)

print("Result of subtraction:")
for row in result:
    print(row)
