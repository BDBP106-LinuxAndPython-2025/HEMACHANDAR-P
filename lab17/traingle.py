#!/usr/bin/python3

import math

# Function to calculate area of triangle
def area_of_triangle(a, b, c):
    s = ((a + b + c) / 2)
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

# Test case
a, b, c = 30, 25, 9
print("Sides:", a, b, c)
print("Area of triangle:", area_of_triangle(a, b, c))
