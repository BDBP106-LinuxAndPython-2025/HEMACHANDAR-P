#!usr/bin/python3

#(i) Using the join method.
a = [i for i in range(1, 51)]

# (a) Join numbers using comma
str_comma = ",".join(str(x) for x in a)
print(str_comma)
# Output: "1,2,3,...,50"

# (b) Join numbers using period
str_period = ".".join(str(x) for x in a)
print(str_period)
# Output: "1.2.3....50"

# (c) Join numbers using '—'
str_dash = "—".join(str(x) for x in a)
print(str_dash)
# Output: "1—2—3—...—50"

# (d) Create a string listing number and its square line by line
lines = [f"{x} {x**2}" for x in a]
result = "\n".join(lines)
print(result)
# Output:
# 1 1
# 2 4
# 3 9
# ...
# 50 2500


