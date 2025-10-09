#!/usr/bin/python3

#(1) Write a program to convert temperature in Celsius to Fahrenheit using map function.

#Fahrenheit = (Celsius * 9/5) + 32
celsius_temps = [0, 10, 20, 30, 40]

def to_fahrenheit(c):
    return c,int((c * 9/5) + 32)

fahrenheit_temps = list(map(to_fahrenheit, celsius_temps))
print(fahrenheit_temps)

#(2) Write the above program using lambda expression.
c= [0, 10, 20, 30, 40]
fahrenheit_temps = list(map(lambda c: (c * 9/5) + 32, c))
print(fahrenheit_temps)
