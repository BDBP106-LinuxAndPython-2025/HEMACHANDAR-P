#!/usr/bin/python3
import email
# (5) Write a Python script that scans through a given piece of text and extracts all unique
# email addresses from it.
import time
import re
pattern=r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
# text=str(input("Enter the text: "))
# time=time.sleep(5)
text = """Contact us at help@ibab.ac.in or admin@python.org.
You can also mail support@ibab.ac.in , if they are not
responding to mail,then mail to 255hsbd010@gmail.com and 255hsbd010@gmail.com"""
# emails =re.findall(pattern, text)
# print(emails)
emails = set(re.findall(pattern, text))
print(emails)
