#!/usr/bin/python3

# (6) Write an interactive calculator
# where the user enters a formula, such as 5 + 10, and the program evaluates it.
# Handle exceptions like incorrect input.

class FormulaError(Exception):
    """Custom exception for invalid formulas."""
    pass

while True:
    try:
        # User input
        user_input = input("Enter a formula (e.g., 5 + 10) or 'quit' to exit: ")

        if user_input.lower() == 'quit':
            break

        # Split input into parts
        parts = user_input.split()

        # Check if input has exactly 3 parts
        if len(parts) != 3:
            raise FormulaError("Formula must consist of 3 parts: number operator number.")

        # Convert first and third input to float
        num1 = float(parts[0])
        num2 = float(parts[2])
        operator = parts[1]

        # Check for valid operator
        if operator not in ['+', '-']:
            raise FormulaError("Invalid operator. Only + and - are allowed.")

        # Perform calculation
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2

        print(f"Result: {result}")

    except ValueError:
        print("Invalid number format. Please enter valid numbers.")
    except FormulaError as fe:
        print(fe)
