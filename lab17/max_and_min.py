#!/usr/bin/python3
#(3) Write a program to find the maximum and minimum values of a dictionary.

numbers = {
    '1': '100',
    '2': '200',
    '3': '300',
    '4': '400',
    '5': '500',
    '6': '600',
    '7': '700',
}
#keys = [int(v) for v in numbers.keys()]
# Convert the values to integers
values = [int(v) for v in numbers.values()]
max_value = max(values)
min_value = min(values)

#for val in values[1:]:
#    if val > max_value:
#        max_value = val
#    if val < min_value:
#        min_value = val

print(f'Maximum value: {max_value}')
print(f'Minimum value: {min_value}')
