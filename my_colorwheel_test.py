import numpy as np
import matplotlib.pyplot as plt
import colorsys as cs

<<<<<<< HEAD
N = 200
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

# def Imagedash():

# 	N = 1000
# 	radii = np.linspace(0,1,N)
# 	thetas = np.linspace(0,2*np.pi,N)
# 	t = [] #list of thetas
# 	r = [] #list of radii
# 	c = [] #list of full of three component list, 3*n dimensional list

# 	# create lists with all possible hs values with v set to 1 (first normalize, then convert to RGB)
# 	for theta in thetas: #nested for loop
# 		for radius in radii:
# 			t.append(theta)
# 			r.append(radius)
# 			c.append(cs.hsv_to_rgb(theta/(2*np.pi),radius,1)) #normalize all theta
# 			# 1 at the end corresponds to brightness

# 	fig = plt.figure()
# 	ax = fig.add_subplot(111, projection='polar')
# 	c = ax.scatter(t, r, c=c, alpha=1.0) #has to take RGB values
# 	plt.axis('off')

# 	# trying to plot example colors onto colorwheel now; hasn't worked so far
# 	# rgb_test = np.array([255,0,0],[0,128,0],[0,0,255]) #red, green, and blue
# 	# t_plot = []
# 	# r_plot = []
# 	# for color in rgb_test:
# 	# 	t_plot.append(color[0]/255*2*np.pi)
# 	# 	r_plot.append(color[1]/255)

# 	# ax.scatter(t_plot,r_plot,linestyle='xk-')

# 	plt.show()

# x = Imagedash()
# print(x)
# >>>>>>> 5a5af7845054efe1f7ff65be76db981e6529cea1
=======

N = 100
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

>>>>>>> d1517309544c2a3a90c686cb34835a1b318668f4
