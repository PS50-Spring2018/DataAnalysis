from matplotlib import pyplot as plt
from matplotlib import image as img
from matplotlib import gridspec as grd
import seaborn as sns
import numpy as np
import colorsys as cs

N = 1000
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

<<<<<<< HEAD
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='polar')
# c = ax.scatter(t, r, c=c, alpha=1.0) #has to take RGB values
# plt.axis('off')
=======
fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')
c = ax.scatter(t, r, c=c, alpha=1.0) #has to take RGB values
>>>>>>> d1517309544c2a3a90c686cb34835a1b318668f4

# trying to plot example colors onto colorwheel now; hasn't worked so far
# rgb_test = np.array([255,0,0],[0,128,0],[0,0,255]) #red, green, and blue
# t_plot = []
# r_plot = []
# for color in rgb_test:
# 	t_plot.append(color[0]/255*2*np.pi)
# 	r_plot.append(color[1]/255)

# ax.scatter(t_plot,r_plot,linestyle='xk-')

x = [1,2,4]
y = [2,5,6]
x2 = [0.1,0.24,0.53]
ourim = img.imread('Cat03.jpg')
gs =grd.GridSpec(2,3)
ax1 = plt.subplot2grid((2,3),(0,0))
ax2 = plt.subplot2grid((2,3),(0,1))
ax3 = plt.subplot2grid((2,3),(0,2))
ax4 = plt.subplot2grid((2,3),(1,0), colspan=2)
ax5 = plt.subplot2grid((2,3),(1,2), projection = 'polar')
ax1.errorbar(x,y,color='r',yerr=x2)
ax4.errorbar(x2,x,yerr=y)
ax2.imshow(ourim)
ax5.scatter(t, r, c=c, alpha=1.0)
<<<<<<< HEAD
ax5.xaxis.set_visible(False)
ax5.yaxis.set_visible(False)
ax2.xaxis.set_visible(False)
ax2.yaxis.set_visible(False)
# for s in range(1,100):
# 	x = np.random.rand(3)
# 	ax3.clear()
# 	ax3.plot(y,x)
# 	plt.pause(0.1)
=======
ax2.xaxis.set_visible(False)
ax2.yaxis.set_visible(False)
for t in range(1,100):
	x = np.random.rand(3)
	ax3.clear()
	ax3.plot(y,x)
	plt.pause(0.1)
>>>>>>> d1517309544c2a3a90c686cb34835a1b318668f4

plt.show()

