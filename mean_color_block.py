import numpy as np
import matplotlib.pyplot as plt
import colorsys as cs



x = range(3)
y = np.zeros(len(x))
color = np.array([[255,0,0],[0,255,127],[0, 128, 0]])
color = color/255

fig = plt.figure()
ax = fig.add_subplot(111)
c = ax.scatter(x, y, c=color, alpha=1.0, marker = 's',s=500) #has to take RGB values
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

