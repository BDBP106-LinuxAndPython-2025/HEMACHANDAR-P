#!/usr/bin/python3

#(14) Write a code to get the Fibonacci numbers beginning with f0 = 0 and f1 = 1 up to f25.

a=0
b=1
print(a)
print(b)
for i in range(1,25):
    c=a+b
    print(c)
    b=c
    a=b
