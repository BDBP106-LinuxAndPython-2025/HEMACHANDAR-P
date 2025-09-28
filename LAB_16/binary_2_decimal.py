#!/usr/bin/python3

#(1) Write a script to convert the binary number B into decimal.

A=int(input('Enter a number: '))
binary=""
remainder=0
if A==0:
    binary="0"
elif A==1:
    binary="1"
else:
    while A>0:
     remainder=A%2
     binary = str(remainder) + binary
     A = A // 2
print(f' the binary value number is: {binary}')