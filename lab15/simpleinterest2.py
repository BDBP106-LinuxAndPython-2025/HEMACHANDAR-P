#!/usr/bin/python3
#(2) Write a program to find the simple interest and the amount with simple interest included.
#The inputs should be the principal, rate of interest in percentage per annum and the
#time in years.

principal=int(input("Enter amount: "))
years=int(input("Enter years: "))
rate_of_interest=int(input("Enter rate of interest: "))

simple_interest=(principal*rate_of_interest*years/100)

total=principal+simple_interest
print(total)

