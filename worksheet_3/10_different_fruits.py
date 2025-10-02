#!/usr/bin/python3

#Define a dictionary containing 10 fruits and their colours. Make sure that the colours
#are repeated as values. Write a loop to iterate over the key-value pairs, and check which
#all fruits are green in colour (this means that your dictionary should contain at least two
#fruits with green as its value (for this example to work well).

fruits = {
    'lime': 'green',
    'mango': 'yellow',
    'avocado': 'green',
    'plum': 'purple',
    'grapefruit': 'pink',
    'cucumber': 'green',
    'pomegranate': 'red',
    'fig': 'purple',
    'guava': 'green',
    'papaya': 'orange'
}
fruits_which_are_in_green=[]
for fruit,color in fruits.items():
    if color == 'green':
        fruits_which_are_in_green.append(fruit)
print(fruits_which_are_in_green)