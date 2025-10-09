#!/usr/bin/python3
import time


# (10) Write a decorator measure_time to calculate how long a function takes to run. Use it
# on the above function calculating population growth that loops 1 million iterations.

def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(result)
        end = time.time()
        print(f"{func.__name__} took {end - start} seconds")
        return result
    return wrapper

