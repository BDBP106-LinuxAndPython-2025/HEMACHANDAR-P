#!/usr/bin/python3

#(13) Write a program to concatenate a list of strings to make a sentence using reduce function.

from functools import reduce
dialogue = ["Unga", "vaai", "unga", "urutu"]

# Concatenate with spaces using reduce
sentence = reduce(lambda x, y: x + " " + y, dialogue)
print(sentence)
