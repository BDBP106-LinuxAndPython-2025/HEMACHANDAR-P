#!/usr/bin/python3
# (8) Write a function protein_energy(temp) with an inner function
# calculate_free_energy(enthalpy, entropy) that computes ∆G = ∆H − T ∆S. Use
# random or user-input ∆H, ∆S and return stability ('stable’ if ∆G < 0).


def protein_energy(temp):
    def calculate_free_energy(enthalpy, entropy):
        delta_g = enthalpy - temp * entropy
        return delta_g

    # Sample values; can use random or user input
    h = float(input("Enter enthalpy (∆H): "))
    s = float(input("Enter entropy (∆S): "))

    delta_g = calculate_free_energy(h, s)

    if delta_g < 0:
        return "Stable"
    else:
        return "Unstable"

print(protein_energy(310))  # temperature in Kelvin
