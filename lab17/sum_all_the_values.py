#!/usr/bin/python3
from os.path import split

#(2) Write a program to sum all the values of a dictionary.
#I have done for both the keys and values but if we need separately i should do that

numbers= {
    '1':'100',
    '2':'200',
    '3':'300',
    '4':'400',
    '5':'500',
    '6':'600',
    '7':'700',
}

total_keys = sum(int(k) for k in numbers.keys())
total_values = sum(int(v) for v in numbers.values())

total = total_keys + total_values
print(f'The sum of keys and values is {total}')

