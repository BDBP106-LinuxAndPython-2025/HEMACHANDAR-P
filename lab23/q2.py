#!/usr/bin/python3

# (2) Write a regular expression that matches integers from 0 to 255. (Note that this is different
# from the question above. Implement this in a script and test for various possibilities.
import re
pattern = r"^([0-9]|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])$"
tests = str(input("Enter number to check: "))
# tests = ['0', '9', '10', '255', '256']
# for t in tests:
print(tests, bool(re.match(pattern, tests)))
# for t in tests:
#print(tests, bool(re.match(pattern, tests)))
# tests = ['000', '255', '257', '099', '19', '252','999','9']
# for t in tests:
#     print(t, bool(re.match(pattern, t)))
