import numpy as np
from scipy.integrate import quad

# Define the functions
def f(x):
    return np.exp(-x**2)

def g(x):
    return x**2

# Integrate f(x) and g(x) over the range from -10 to 10
area_f, _ = quad(f, -10, 10)
area_g, _ = quad(g, -10, 10)

# Calculate the area between the curves
area_between_curves = area_f - area_g

print(round(area_between_curves, 4))
