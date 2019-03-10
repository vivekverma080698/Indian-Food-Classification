import os
from shutil import copyfile

classLabel = 1
for folder in os.listdir('.'):
	print(folder)
	imageNumber = 1
	for images in os.listdir(folder):
		src = './' + folder + '/' + images
		dest2 = './NameConv/'+folder + '/'+images
		dest = './NameConv/'+folder + '/'+str(imageNumber)+'_'+str(classLabel)+'.jpg'
		directory = './NameConv/'+folder
		if not os.path.exists(directory):
			os.makedirs(directory)
		copyfile(src, dest2)
		os.rename(dest2,dest)
		imageNumber += 1
	classLabel += 1		