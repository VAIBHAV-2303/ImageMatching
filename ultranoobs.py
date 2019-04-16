import matplotlib.image as mpimg
import glob
import numpy as np
import math

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

framespath = glob.glob("./Test/frames/*.jpg")
slidespath = glob.glob("./Test/slides/*.jpg")
framespath.sort()
slidespath.sort()


slides = []

# Converting to rgb and then normalizing
for i in slidespath:
	im = mpimg.imread(i)
	gray = rgb2gray(im)
	gray = gray.astype(np.int32)
	slides.append((gray-np.mean(gray))/math.sqrt(np.var(gray)))
	    

for i in range(len(framespath)):
	im = mpimg.imread(framespath[i])
	gray = rgb2gray(im)
	gray = gray.astype(np.int32)
	gray = (gray-np.mean(gray))/math.sqrt(np.var(gray))

	curmax = -1e15
	ans = -1
	for j in range(len(slides)):
		try:
			temp = np.sum(np.multiply(gray, slides[j]))
			if temp > curmax:
				curmax = temp
				ans = j
		except:
			pass
	print(framespath[i].split('/')[3], slidespath[ans].split('/')[3])