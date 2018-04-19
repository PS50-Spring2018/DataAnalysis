import numpy as np
import matplotlib.pyplot as plt
import colorsys as cs

N = 1000
radii = np.linspace(0,1,N)
thetas = np.linspace(0,2*np.pi,N)
t = []
r = []
c = []

# create lists with all possible hs values with v set to 1 (first normalize, then convert to RGB)
for theta in thetas:
	for radius in radii:
		t.append(theta)
		r.append(radius)
		c.append(cs.hsv_to_rgb(theta/(2*np.pi),radius,1))

fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')
c = ax.scatter(t, r, c=c, alpha=1.0)
plt.axis('off')

# trying to plot example colors onto colorwheel now; hasn't worked so far
rgb_test = np.array([[255,0,0],[0,128,0],[0,0,255]]) #red, green, and blue
t_val = []
r_val = []
for color in rgb_test:
	r, g, b = color[0], color[1], color[2]
	hsv = cs.rgb_to_hsv(r,g,b)
	t_val.append(hsv[0]*2*np.pi)
	r_val.append(hsv[1])

d = ax.plot(t_val,r_val, 'ko-')

plt.show()