# Source: https://stackoverflow.com/questions/39619128/plotting-direction-field-in-python
# Script for Elementary Differential Equations, §1.1 (Boyce and DiPrima)

from matplotlib.pyplot import cm
import matplotlib.pyplot as plt
import numpy as np

nx, ny = .3, .3
x = np.arange(-10, 10, nx)
y = np.arange(-10, 10, ny)
X, Y = np.meshgrid(x, y)

dy = -Y * (5 - Y)
dx = np.ones(dy.shape)

color = dy
lw = 1
plt.streamplot(X, Y, dx, dy, color=color, density=1., cmap='jet', arrowsize=1)
plt.show()
