import numpy as np
import matplotlib.pyplot as plt
import colorsys as cs


N = 200
radii = np.linspace(0,1,N)
thetas = np.linspace(0,2*np.pi,N)
t = [] #list of thetas
r = [] #list of radii
c = [] #list of full of three component list, 3*n dimensional list

# create lists with all possible hs values with v set to 1 (first normalize, then convert to RGB)
for theta in thetas: #nested for loop
	for radius in radii:
		t.append(theta)
		r.append(radius)
		c.append(cs.hsv_to_rgb(theta/(2*np.pi),radius,1)) #normalize all theta
		# 1 at the end corresponds to brightness

fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')
c = ax.scatter(t, r, c=c, alpha=1.0) #has to take RGB values
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

