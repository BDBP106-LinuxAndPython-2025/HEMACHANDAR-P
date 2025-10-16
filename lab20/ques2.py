# main.py

from math_utils import math_utils,string_utils

# For numbers 34 and 45
a=int (input("enter first number: "))
b=int (input("enter second number: "))

print(f'Math operations for {a} and {b} are:')
print("Addition:", math_utils.add(a, b))
print("Subtraction:", math_utils.subtract(a, b))
print("Multiplication:", math_utils.multiply(a, b))
print("Division:", math_utils.divide(a, b))
print("Remainder:", math_utils.remainder(a, b))

# For strings 'BDBH' and '101'
s1=input("enter first string: ")
s2=input("enter second string: ")

print()
print(f'String operations for {s1} and {s2} are:')
print("To Lowercase:", string_utils.lowercase(s1))
print("To Uppercase:", string_utils.uppercase(s2))
print("Concatenation:", string_utils.concatenate(s1, s2))
