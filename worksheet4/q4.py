#!/usr/bin/python3
#
# (4) Write a function enzyme_activity(name,subs_conc) that accepts the name of the enzyme
# and substrate concentration as parameters. This will have an inner function called
# michelis_menten(Vmax,Km) that computes the reaction rate
# v = V max × [S]/ Km + [S]
# and the outer function should return the reaction rate for given values. Write a main
# program that demonstrates the use of this inner and outer function with a meaningful
# example.

def enzyme_activity(name, subs_conc):
    def michelis_menten(Vmax, Km):
        return (Vmax * subs_conc) / (Km + subs_conc)
    # Example parameters for demonstration
    Vmax = 100
    Km = 50
    rate = michelis_menten(Vmax, Km)
    print(f"Enzyme: {name}, Substrate concentration: {subs_conc}, Reaction rate: {rate}")
    return rate
# Example usage
enzyme_activity("Lactase", 30)
