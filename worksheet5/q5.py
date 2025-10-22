#!/usr/bin/python3

# (5) Define a module called prime that contains a function isPrime()
# that checks if a number is prime or not. Use this module and function to print the first N prime numbers.

# prime.py

def isPrime(n):
    """
    Check if a number n is prime.
    A prime number is a number greater than 1 that has no divisors other than 1 and itself.
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def printPrimes(N):
    """
    Print the first N prime numbers.
    """
    count = 0
    num = 2
    while count < N:
        if isPrime(num):
            print(num, end=" ")
            count += 1
        num += 1

