#!/usr/bin/pyhton3
#(3) Write a Python script to check if a given string contains an email address or not.

import re
#[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}
pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]"
tests = str(input("Enter a sequence to check if it matches pattern: "))
print(tests, bool(re.search(pattern, tests)))

