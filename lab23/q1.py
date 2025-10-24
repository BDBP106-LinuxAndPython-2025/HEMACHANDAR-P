#!/usr/bin/python3

# (1) Write a regular expression that accepting a 3-digit integer between 000 and 255. Imple-
# ment this in a script and test it for various possibilities
import re

pattern = r"^([01]\d\d|2[0-4]\d|25[0-5])$"
tests = str(input("Enter number to check: "))

# for t in tests:
print(tests, bool(re.match(pattern, tests)))
# tests = ['000', '255', '257', '099', '19', '252','999','9']
# for t in tests:
#     print(t, bool(re.match(pattern, t)))







