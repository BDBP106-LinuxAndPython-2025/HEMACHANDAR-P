#!/usr/bin/python3

people = [
    "aheli biswas",
    "anchal kumari",
    "aisha khan",
    "anshu sharma",
    "atharva kadam",
    "chiranjeevi sai deva",
    "disha nayak",
    "hariharan mahendran",
    "harish kumar ravi",
    "hemachandar poochami",
    "himiksha singh",
    "inshika thakur",
    "ishita badola"
]

# (a) Convert each to uppercase
people_upper = [p.upper() for p in people]
print(people_upper)
# Output: ['AHELI BISWAS', 'ANCHAL KUMARI', ...]

# (b) Swap first name and surname
people_swapped = [' '.join(p.split()[::-1]) for p in people]
print(people_swapped)
# Output: ['biswas aheli', 'kumari anchal', ...]

# (c) Join as 'First.Last' with uppercase first letters
# For names with more than 2 parts (like 'chiranjeevi sai deva'), we'll consider first and last words
people_formatted = [
    f"{p.split()[0].capitalize()}.{p.split()[-1].capitalize()}" for p in people
]
print(people_formatted)
# Output: ['Aheli.Biswas', 'Anchal.Kumari', 'Aisha.Khan', 'Anshu.Sharma', ...]
