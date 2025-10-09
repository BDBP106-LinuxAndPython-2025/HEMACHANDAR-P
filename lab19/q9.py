#!/usr/bin/python3

# (9) Write a function population_growth(initial,rate, time) that defines an inner function
# exponential_growth() using the formula N(t) = N0 + exp(rate ∗ time) where N0
# represents the initial population and N(t) is population after time t. The inner function
# returns the population after time, and the outer function rounds and prints it.

def population_growth(initial, rate, time):
    def exponential_growth():
        # Calculate population using N(t) = N0 + exp(rate * time)
        from math import exp
        return initial + exp(rate * time)

    population = exponential_growth()
    print(round(population))

population_growth(1000, 0.05, 10)
