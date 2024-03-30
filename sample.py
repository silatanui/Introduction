import numpy as np
import matplotlib.pyplot as plt

# Define the functions
def f(x):
    return np.exp(-x**2)

def g(x):
    return x**2

# Generate x values
x = np.linspace(-3, 3, 1000)

# Plot the curves
plt.plot(x, f(x), label='$y = e^{-x^2}$')
plt.plot(x, g(x), label='$y = x^2$')

# Fill the area between the curves
x_fill = np.linspace(-3, 3, 1000)
y_fill_1 = f(x_fill)
y_fill_2 = g(x_fill)
plt.fill_between(x_fill, y_fill_1, y_fill_2, where=(y_fill_1 >= y_fill_2), color='gray', alpha=0.5)

# Add labels and legend
plt.xlabel('x')
plt.ylabel('y')
plt.title('Area Between Curves')
plt.legend()

# Show plot
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.show()
