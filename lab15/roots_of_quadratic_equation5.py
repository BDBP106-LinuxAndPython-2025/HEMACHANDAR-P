#!/bin/usr/pyhton3

#Write a program to find the roots of a quadratic equation. Figure out what the inputs
#should be and also have provision to deal with cases where you end up getting complex
#roots.
import cmath

a=complex(input("Enter first number(a): "))
b=complex(input("Enter second number(b): "))
c=complex(input("Enter third number(c): "))

roots_of_quadratic_equation=(-b+cmath.sqrt(b**2-4*a*c))/(2*a),(-b-cmath.sqrt(b**2-4*a*c))/(2*a)

print(roots_of_quadratic_equation)