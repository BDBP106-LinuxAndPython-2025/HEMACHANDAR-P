#!/usr/bin/python3


# (4) Write a program to filter out the odd elements of the Fibonacci series for the first n
# terms.


n = 10  # You can change this to any number
fib_series = []
a = 0
b = 1
# Generate Fibonacci series
fib_series.append(a)
if n > 1:
    fib_series.append(b)
for i in range(2, n):
    c = a + b
    fib_series.append(c)
    a = b
    b = c
# Filter out odd numbers (keep even numbers)
even_fib = list(filter(lambda x: x % 2 == 0, fib_series))

print("Fibonacci series:", fib_series)
print("Even elements (odd filtered out):", even_fib)
