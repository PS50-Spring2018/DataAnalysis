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
# rgb_test = np.array([255,0,0],[0,128,0],[0,0,255]) #red, green, and blue
# t_plot = []
# r_plot = []
# for color in rgb_test:
# 	t_plot.append(color[0]/255*2*np.pi)
# 	r_plot.append(color[1]/255)

# ax.scatter(t_plot,r_plot,linestyle='xk-')

plt.show()

