#!/usr/bin/python3
import math

# (10) Write a function called nextPrime that finds and returns the first prime number larger
# than some integer, n. The value of n will be passed to the function as its only parameter.
# The main program should read an integer from the user and display the first prime
# number larger than the entered value.
import math

def nextPrime(n):
    possible_prime = n + 1

    while True:
        if possible_prime <= 3:
            if possible_prime > 1:
                return possible_prime
        else:
            # Check divisibility from sqrt down to 3
            limit = int(math.sqrt(possible_prime))
            is_prime = True
            for divisor in range(limit, 2, -1):
                if possible_prime % divisor == 0:
                    is_prime = False
                    break
            if is_prime:
                return possible_prime

        possible_prime += 1

# Main program
num = int(input("Enter an integer: "))
print("The first prime number larger than", num, "is", nextPrime(num))
