import numpy as np
import matplotlib.pyplot as plt


# Fixing random state for reproducibility
np.random.seed(19680801)

# Compute areas and colors
N = 100
r = np.ones(N)
theta = np.linspace(0, 2*np.pi, N)
area = 200 * r**2
colors = theta
colors = np.array([np.linspace(0, 1, N), 0*np.ones(N), 0.5*np.ones(N)]).T

fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=1.00)
plt.show()