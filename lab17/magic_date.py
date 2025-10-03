#!/usr/bin/python3

#(11) A magic date is a date where the date multiplied by the month is equal to the two-digit
#year. For example, June 10, 1960 is a magic date because June is the sixth month, and
#6 times 10 is 60 which is the two-digit year. Write a function that determines whether
#or not a date is a magic date. Use your function to create a main program that finds
#and displays all of the magic dates in the 20th century.

def is_magic_date(day, month, year):
    two_digit_year = year % 100
    return day * month == two_digit_year

def main():
    # Get input from the user in order: day, month, year
    day = int(input("Enter day (1-31): "))
    month = int(input("Enter month (1-12): "))
    year = int(input("Enter year (e.g., 1960): "))

    # Check if it's a valid date
    try:
        import datetime
        datetime.date(year, month, day)  # This will raise ValueError if invalid
    except ValueError:
        print("Invalid date. Please enter a real calendar date.")
        return

    # Check if it's a magic date
    if is_magic_date(day, month, year):
        print(f"{day:02d}-{month:02d}-{year} is a MAGIC date!")
    else:
        print(f"{day:02d}-{month:02d}-{year} is NOT a magic date.")

# Run the main function
main()

