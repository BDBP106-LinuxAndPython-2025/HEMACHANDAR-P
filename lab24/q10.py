# Gaussian function
import numpy as np
import matplotlib.pyplot as plt

def gaussian(x, sigma):
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-x ** 2 / (2 * sigma ** 2))


# x range
x = np.linspace(-10, 10, 1000)
sigmas = [1, 1.5, 2]

plt.figure(figsize=(10, 6))
for sigma in sigmas:
    plt.plot(x, gaussian(x, sigma), label=f'σ = {sigma}')

plt.title('Normalized Gaussian Functions')
plt.xlabel('x')
plt.ylabel('g(x)')
plt.legend()
plt.grid(True)
plt.show()
