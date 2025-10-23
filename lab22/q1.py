#!/usr/bin/python3

# (1) Create a logging decorator to record function calls, arguments, and return values. For
# example, if we have an add function shown below and invoke it as add(2,3), create a
# decorator that prints the following:

def log_function(hems):
    def wrapper(*args):
        print(f"Calling {hems.__name__} with args: {args}")
        result = hems(*args)
        print(f"{hems.__name__} returned: {result}")
        return result
    return wrapper

@log_function
def add(a, b):
    return a + b

@log_function
def sub(a, b):
    return a - b

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
# print(add(a,b))
# print(sub(a,b))
add(a,b)
sub(a,b)
