#!/usr/bin/python3

#(1) Explain the various ways of importing module contents with examples.

# 1. Import the entire module
import math
print("1. Full import:", math.sqrt(16))

# 2. Import with an alias
import math as hems
print("2. Alias import:", hems.sqrt(25))

# 3. Import specific items
from math import sqrt, pi
print("3. Specific import - sqrt:", sqrt(9))
print("4. Specific import - pi:", pi)

# 4. Import all contents
from math import *
print("5. Import all - sqrt:", sqrt(36))
print("6. Import all - pi:", pi)

# 5. Dynamic import using __import__()
math_module = __import__('math')
print("7. Dynamic import:", math_module.sqrt(49))


