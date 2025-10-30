import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 points from -20 to 20
x = np.linspace(-20, 20, 1000)

# Compute functions
f1 = np.log(1 / (np.cos(x)**2))
f2 = np.log(1 / (np.sin(x)**2))

# Plot
plt.figure(figsize=(12,6))
plt.plot(x, f1, label='f1(x) = ln(1/cos^2(x))')
plt.plot(x, f2, label='f2(x) = ln(1/sin^2(x))')
plt.ylim(-10, 10)  # Limit y for better visualization
plt.axhline(0, color='black', linewidth=0.5)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plots of f1(x) and f2(x)')
plt.legend()
plt.show()
