#!/usr/bin/python3
#(7) Write a program with a function to find whether a given triangle with sides a, b, c is
#isosceles, scalene or equilateral triangle, also provide a test case output from the program.

def sides_of_triangle(a,b,c):
    if a == b == c:
        print("equilateral triangle")
    elif a == b or a == c or b == c:
        print("isosceles triangle")
    else:
        print("scalene triangle")

sides_of_triangle(6,6,6)


