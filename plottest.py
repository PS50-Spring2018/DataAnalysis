from matplotlib import pyplot as plt
from matplotlib import image as img
from matplotlib import gridspec as grd
import seaborn as sns
import numpy as np
x = [1,2,4]
y = [2,5,6]
x2 = [0.1,0.24,0.53]
ourim = img.imread('Cat03.jpg')
gs =grd.GridSpec(2,3)
ax1 = plt.subplot2grid((2,3),(0,0))
ax2 = plt.subplot2grid((2,3),(0,1))
ax3 = plt.subplot2grid((2,3),(0,2))
ax4 = plt.subplot2grid((2,3),(1,0), colspan=3)
ax1.errorbar(x,y,color='r',yerr=x2)
ax4.errorbar(x2,x,yerr=y)
ax2.imshow(ourim)
ax2.xaxis.set_visible(False)
ax2.yaxis.set_visible(False)
for t in range(1,100):
	x = np.random.rand(3)
	ax3.clear()
	ax3.plot(y,x)
	plt.pause(0.1)

plt.show()