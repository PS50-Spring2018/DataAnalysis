import numpy as np
from matplotlib import pyplot as plt
def Initialize(): #to initialize the dashboard
	meanR = []
	meanG = []
	meanB = []
	varR = []
	varG = []
	varB = []
	hsvholder = []
def Run(rgb): #rgb is a numpy array in the format [[meanR,meanG,meanB],[varR,varG,varB]]; rgb should be 
#the most recently updated data

	#Plots RGB vs time
	meanR.append(rgb[0][0])
	meanG.append(rgb[0][1])
	meanB.append(rgb[0][2])
	varR.append(rgb[1][0])
	varG.append(rgb[1][1])
	varB.append(rgb[1][2])
	plt.errorbar(x)
	xvals = arange(len(meanR))
	plt.errorbar(xvals,meanR,color='r',yerror=varR)
	plt.errorbar(xvals,meanG,color='g',yerror=varG)
	plt.errorbar(xvals,meanB,color='b',yerror=varB)

	#Converting RGB to HSV
	rprime = meanR/255
	gprime = meanG/255
	bprime = meanB/r55
	cmax = max([rprime,gprime,bprime])
	cmin = min([rprime,gprime,bprime])
	cmaxind = np.argmax([rprime,gprime,bprime])
	
	if 
