#!/usr/bin/python3

#(8) In the above exercise, let’s use an in-built decorator function called lru_cache, where
# lru stands for least recently used – It caches/stores the results of function calls, so
# that if the same input occurs again, it reuses the stored result instead of recomputing it.
# Least recently used means that it keeps the most recent results and discards the oldest
# ones if the cache gets full. We have control over the size of this cache, An example usage
# is given below.
# from functools import lru_cache
# @lru_cache(maxsize=None)
# def factorial(n):
# if n==0 or n==1: return 1
# if n>1: return n*factorial(n-1)
# (i) Use a similar setup for the Fibonacci series calculation with maxsize=5. What is
# the time difference you see with and without the use of lru_cache?
#
# (ii) Provide a docstring with ‘This function outputs the sum of n Fibonacci num-bers’
# inside the function. Print fibonacci.__doc__ and observe the output.
#
# (iii) Use a custom decorator log_time to print the datetime.now() value at entry
# and exit for every func.__name__ call with the n (args) value.

from functools import lru_cache
from datetime import datetime
import time

# (iii) Custom decorator to log time at entry and exit for every function call
def log_time(func):
    def wrapper(*args, **kwargs):
        # Log time before function execution
        print(f"{func.__name__} started at {datetime.now()} with arguments {args}")
        result = func(*args, **kwargs)
        # Log time after function execution
        print(f"{func.__name__} finished at {datetime.now()}")
        return result
    return wrapper

# (i) Fibonacci function with LRU cache (maxsize=5) and custom decorator
@log_time
@lru_cache(maxsize=5)  # Using LRU cache to store results and avoid recomputing
def fibonacci(n):
    """
    This function outputs the sum of n Fibonacci numbers.
    """
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Test the time taken with and without LRU cache
start_time = time.time()
print(f"Fibonacci(35) with LRU cache: {fibonacci(35)}")  # With LRU cache
end_time = time.time()
print(f"Execution time with LRU cache: {end_time - start_time:.5f} seconds")

# Fibonacci function without LRU cache
def fibonacci_no_cache(n):
    if n <= 1:
        return n
    return fibonacci_no_cache(n-1) + fibonacci_no_cache(n-2)

# Test the time taken without LRU cache
start_time = time.time()
print(f"Fibonacci(35) without LRU cache: {fibonacci_no_cache(35)}")  # Without LRU cache
end_time = time.time()
print(f"Execution time without LRU cache: {end_time - start_time:.5f} seconds")

# (ii) Print the docstring of the fibonacci function
print("\nDocstring of fibonacci function:")
print(fibonacci.__doc__)

