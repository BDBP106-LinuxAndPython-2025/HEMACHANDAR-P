#!/usr/bin/python3

# How Python Knows Where to Search for Modules

import sys

print(" Python searches for modules in the following locations:\n")

for i, path in enumerate(sys.path, start=1):
    print(f"{i}. {path}")


