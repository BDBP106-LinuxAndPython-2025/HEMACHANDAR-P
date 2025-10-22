#!/usr/bin/python3
# (4) Write a Python function checkList that accepts a list and an index, and prints the
# element of the list at the index position. Catch the IndexError and TypeError and
# display appropriate messages. Call the function for (a) number list and index, (b) A
# string input and index, (c) A boolean value (True) and index and (d) A string input and
# incorrect index.
def checkList(lst, index):
    try:
        print(f"Element at index {index}:", lst[index])
    except IndexError:
        print("IndexError: The index is out of range.")
    except TypeError:
        print("TypeError: Provided input is not a list or index is not an integer.")

user_list =eval(input("Enter a list (e.g., [1, 2, 3]): "))
user_index = int(input("Enter the index: "))

checkList(user_list, user_index)

