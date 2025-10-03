#!/usr/bin/python3

#(1) Write a program to iterate over a dictionary and print the key-value pairs.

fruits = {
    'apple': 100,
    'banana': 200,
    'orange': 300,
    'grapes': 400,
    'strawberry': 500,
    'peach': 600,
    'lemon': 700,
}
for key, value in fruits.items():
    print(f'{key}: {value}')