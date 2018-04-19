import numpy as np
import matplotlib.pyplot as plt
import colorsys as cs


N = 200
x_dim = np.linspace(0,1,N)
y_dim = np.linspace(0,1,N)
x = []
y = []
color = []

# create lists with all possible hs values with v set to 1 (first normalize, then convert to RGB)
for x_val in x_dim: #nested for loop
	for y_val in y_dim:
		x.append(x_val)
		y.append(y_val)
		color.append(cs.hsv_to_rgb(0, 0, 1-x_val)) #normalize all theta
		# 1 at the end corresponds to brightness

fig = plt.figure()
ax = fig.add_subplot(111)
c = ax.scatter(x, y, c=color, alpha=1.0) #has to take RGB values
plt.axis('off')

# trying to plot example colors onto colorwheel now; hasn't worked so far
rgb_test = np.array([[173,216,230],[0,0,255],[0,0,139]]) #light blue, blue, and dark blue
x_points = []
y_points = 0.5*np.ones(3)
for color in rgb_test:
	r, g, b = color[0], color[1], color[2]
	hsv = cs.rgb_to_hsv(r,g,b)
	x_points.append(hsv[2]/255)

d = ax.plot(x_points,y_points, 'yo-')


plt.show()

