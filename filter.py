import sys
from PIL import Image

def filter(img, f):
	copyImage = img.copy()
	originalMatrix = img.load() #makes a matrix from an image
	pixels = copyImage.load()
	width, height = img.size #width and height of image

	for i in range(width):
		for j in range(height):
			r = region3x3(img, i, j) 
			pixels[i, j] = f(r)

	return copyImage

def region3x3(img, x, y):
	img.load()
	list = [] 

	# Broken into rows
	list.append(getpixel(img, x-1, y-1))
	list.append(getpixel(img, x, y-1))    #North, index is 1
	list.append(getpixel(img, x+1, y-1)) 

	list.append(getpixel(img, x-1, y))  #West index is 3
	list.append(getpixel(img, x, y))    #Center index is 4
	list.append(getpixel(img, x+1, y))  #East index is 5

	list.append(getpixel(img, x-1, y+1))
	list.append(getpixel(img, x, y+1))  #South index is 7
	list.append(getpixel(img, x+1, y+1)) 

	return list

def getpixel(img, x, y):
	width, height = img.size
	if (x < 0):
		x = 0
	if (x >= width):
		x = width - 1
	if (y >= height):
		y = height - 1
	if (y < 0):
		y = 0
	matrix = img.load()
	return matrix[x, y]

def open(argv):
	if len(argv)<=1:
		print "missing image filename"
		sys.exit(1)
	img = Image.open(argv[1])
	img = img.convert("L") # make greyscale if not already (luminance) 
	return img