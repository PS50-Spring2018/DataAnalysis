def DashUpdate(mean_RGB, var_RGB, image_array): #each input is a numpy array, mean RGB and var RGB should each contain 3 numbers; image_array is a np array that needs to be converted into an image
	meanR.append(mean_RGB[0])
	meanG.append(mean_RGB[1])
	meanB.append(mean_RGB[2])
	varR.append(var_RGB[0])
	varG.append(var_RGB[1])
	varB.append(var_RGB[2])


	beaker.imshow(image_array, interpolation='nearest')
	plt.show()
