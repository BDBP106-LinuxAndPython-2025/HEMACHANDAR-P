#!/usr/bin/python3

# (2) Create a decorator to measure the execution time of a function. Please demonstrate
# using a sample function (add sleep for checking) and a decorator for this sample function
# that measures the execution time.
import time
def measure_time(hems):
    def wrapper(*args):
        start = time.time()
        result = hems(*args)
        end = time.time()
        print(f"Execution time for {hems.__name__}: {end - start:.2f} seconds")
        return result
    return wrapper

@measure_time
def sample_function():
    time.sleep(0.1)
    print("Function completed")

@measure_time
def wanted_function():
    print()
    time.sleep(2)
    print("Function completed by me")



# Example call
sample_function()
wanted_function()



