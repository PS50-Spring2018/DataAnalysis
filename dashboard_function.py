from matplotlib import pyplot as plt
from matplotlib import image as img
from matplotlib import gridspec as grd
import seaborn as sns
import numpy as np
import colorsys as cs

def dashboard(N =200):

	# initialize lists of all-time relevant RGB values
	meanR = []
	meanG = []
	meanB = []
	varR = []
	varG = []
	varB = []


	# the following section plots the colorwheel
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

	# the following section plots the colorbar
	x_dim = np.linspace(0,1,N)
	y_dim = np.linspace(0,1,N)
	x = []
	y = []
	color = []

	for x_val in x_dim:
		for y_val in y_dim:
			x.append(x_val)
			y.append(y_val)
			color.append(cs.hsv_to_rgb(0, 0, 1-x_val))

	# may want to use something like ourim = img.imread('Cat03.jpg') to read image
	# sets up grid
	gs =grd.GridSpec(3,6)
	# specifies which grid squares each subplot spans
	lines = plt.subplot2grid((3,6),(0,0), colspan=2, rowspan =2)
	beaker = plt.subplot2grid((3,6),(0,2), colspan=2, rowspan =2)
	colorbar = plt.subplot2grid((3,6),(2,4), colspan=2)
	squares = plt.subplot2grid((3,6),(2,0), colspan=4)
	colorwheel = plt.subplot2grid((3,6),(0,4), projection = 'polar', colspan=2, rowspan =2)
	
	colorwheel.scatter(t, r, c=c, alpha=1.0)
	colorwheel.xaxis.set_visible(False)
	colorwheel.yaxis.set_visible(False)
	colorwheel.set_title('Tracking through Color Space', fontsize = 8)
	colorwheel.axis('off')

	colorbar.scatter(x, y, c=color, alpha=1.0)
	colorbar.xaxis.set_visible(False)
	colorbar.yaxis.set_visible(False)
	colorbar.axis('off')
	colorbar.set_title('Tracking through Intensity Space', fontsize = 8)
	
	beaker.axis('off')
	beaker.set_title('Latest Beaker Image', fontsize = 8)
	
	lines.set_title('History of Mean RGB Values', fontsize = 8)
	lines.set_xlabel('Iterations', fontsize = 8)
	
	squares.axis('off')
	squares.set_title('Average Beaker Colors and Future Predictions',fontsize = 8)

	# something like the following lines allows plot updating in real time
	# for s in range(1,100):
	# 	x = np.random.rand(3)
	# 	ax3.clear()
	# 	ax3.plot(y,x)
	# 	plt.pause(0.1)

	plt.tight_layout()
	plt.show()


#if __name__=='__main__':

	#dashboard()

