from PIL import Image
import os, sys
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

path = "./Raw_images"
ResizedImg = './ResizedImg'
dirs = os.listdir( path )

def resize():
    for item in dirs:
		newPath = path+'/'+item
		directory = ResizedImg+'/'+item
		if not os.path.exists(directory):
			os.makedirs(directory)
		else:
			continue
		for files in os.listdir(newPath):
			try:
				filepath = newPath+'/'+files
				im = Image.open(filepath)
				imResize = im.resize((224,224),Image.ANTIALIAS)
				imResize.convert('RGB').save(directory+'/'+files,'PNG',optimize=True)			
				print(item,files)
			except:
				print('File Skipped',files)
				
resize()