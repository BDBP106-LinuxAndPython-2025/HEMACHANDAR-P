#!/usr/bin/python3
# (7) Implement the Fibonacci function with parameter n, and
# use a decorator to log the time taken to run the function.

from functools import lru_cache
import time

# Define the Fibonacci function with an LRU cache
@lru_cache(maxsize=100)
def fibonacci(n):
    """
    Return the nth Fibonacci number.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Decorator to measure execution time
def log_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Start the timer
        result = func(*args, **kwargs)
        end_time = time.time()  # End the timer
        print(f"Execution time: {end_time - start_time:.5f} seconds")
        return result
    return wrapper

# Apply the decorator to Fibonacci
@log_time
def fibonacci_with_log(n):
    return fibonacci(n)

# Test the function
print(fibonacci_with_log(100))
