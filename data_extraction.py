import shutil
import glob 

temp = glob.glob("./Dataset/*")
for i in temp:

	# Frames
	for j in range(10):
		try:
			shutil.copyfile(i + "/" + str(j) + ".jpg", './Test/frames/' + i[10:] + '_' + str(j) + '.jpg')
		except:
			pass
	
	# Slides
	shutil.copyfile(i + "/ppt.jpg", './Test/slides/' + i[10:] + '.jpg')
