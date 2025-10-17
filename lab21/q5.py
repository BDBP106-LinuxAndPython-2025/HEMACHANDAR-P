#!/usr/bin/python3
# (5) Write a function that takes two numbers n1 and n2 and an operator description such
# as add, subtract etc. Depending on the operation, perform the operation. Raise a
# ValueError if the operator is not an arithmetic operation such as add, subtract, mul-
# tiplication or division. Catch the ValueError and ZeroDivisionError and print the
# appropriate messages. In the finally block, print a completion message. Call this func-
# tion with different scenarios to test the above exceptions. Take screenshots of the output
# while uploading your labs to GitHub.

def math_operation(n1, n2, operation):
    try:
        if operation == "add":
            result = n1 + n2
        elif operation == "subtract":
            result = n1 - n2
        elif operation == "multiplication":
            result = n1 * n2
        elif operation == "division":
            result = n1 / n2
        else:
            raise ValueError("Invalid operation. Supported: add, subtract, multiplication, division.")
        print(f"Result of {operation} between {n1} and {n2} is {result}")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except ZeroDivisionError:
        print("ZeroDivisionError: Cannot divide by zero.")
    finally:
        print("Operation completed.\n")

# Get inputs from the user
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Enter operation (add, subtract, multiplication, division): ").lower()

    math_operation(num1, num2, op)

except ValueError:
    print("Invalid input! Please enter numeric values for numbers.")
