import matplotlib.image as mpimg
import glob
import numpy as np
import math
from scipy import ndimage
import sys
import os

file_obj = open("20171101_20171005_20171108.txt","w")

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

framespath = os.listdir(sys.argv[2])
slidespath = os.listdir(sys.argv[1])

for frames in range(len(framespath)):
	framespath[frames] = os.path.join(sys.argv[2],framespath[frames])

for slides in range(len(slidespath)):
	slidespath[slides] = os.path.join(sys.argv[1],slidespath[slides])


framespath.sort()
slidespath.sort()

slides = []

# Converting to rgb, applying sobel and then normalizing

for i in slidespath:
	im = mpimg.imread(i)
	gray = rgb2gray(im)

	dx = ndimage.sobel(gray, 1)
	dy = ndimage.sobel(gray, 0)
	gray = np.hypot(dx, dy)
	gray *= 255.0/np.max(gray)

	slides.append((gray-np.mean(gray))/math.sqrt(np.var(gray)))

correct = 0
incorrect = 0

for i in range(len(framespath)):
	im = mpimg.imread(framespath[i])
	gray = rgb2gray(im)

	dx = ndimage.sobel(gray, 1)
	dy = ndimage.sobel(gray, 0)
	gray = np.hypot(dx, dy)
	gray *= 255.0/np.max(gray)

	gray = (gray-np.mean(gray))/math.sqrt(np.var(gray))

	curmax = -1e15
	ans = -1
	for j in range(len(slides)):
		try:
			temp = np.sum(np.multiply(gray, slides[j]))
			if temp >= curmax:
				curmax = temp
				ans = j
		except:
			pass
	file_obj.write(framespath[i].split('/')[len(framespath[i].split('/'))-1] + " " + slidespath[ans].split('/')[len(slidespath[ans].split('/'))-1] + "\n")

file_obj.close()
