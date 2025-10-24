#!usr/bin/python3
# (4) Write a Python script that accepts a line of CSV and checks if the 3rd field contains
# exactly an email address or not, given that there are more than 3 fields.

import re

pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
csv_files = [
    "1,Hems,test@gmail.com,Developer",
    "2,Hari,harishkumar's_mail,Manager",
    "3,Shreyas,shreyas@yahoo.com,Manager",
    "4,Vineeth,vineeth@gmail.com"
]

for line in csv_files:
    fields = line.split(',')
    # print(fields)
    if len(fields) > 3:
        email = fields[2].strip()
        # print(email)
        print(line, bool(re.match(pattern, email)))
