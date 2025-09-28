#!/usr/bin/python3

#(14) Remove all occurrences of an element from a list L

L = [1, 2, 3, 2, 4, 2, 5]
element_to_remove = 2

# Using list comprehension to filter out the element
L = [x for x in L if x != element_to_remove]

print("List after removing", element_to_remove, ":", L)
