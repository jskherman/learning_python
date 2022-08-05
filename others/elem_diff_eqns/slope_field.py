# Source: https://stackoverflow.com/questions/39619128/plotting-direction-field-in-python
# Script for Elementary Differential Equations, §1.1 (Boyce and DiPrima)

from matplotlib.pyplot import cm
import matplotlib.pyplot as plt
import numpy as np

nx, ny = .3, .3             # increments
x = np.arange(-3, 3, nx)    # sample from -3 to 3 in the x-axis
y = np.arange(-3, 3, ny)    # sample from -2 to 2 in the y-axis
X, Y = np.meshgrid(x, y)    # Create meshgrid

dy = X + np.sin(Y)                 # The Differential Equation
dx = np.ones(dy.shape)

plt.quiver(X, Y, dx, dy, color="Teal", headlength=7)
plt.title('Direction/Slope Field')
plt.show()
