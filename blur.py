import sys
from PIL import Image

def blur(img):
	copyImage = img.copy()
	originalMatrix = img.load() #makes a matrix from an image
	pixels = copyImage.load()
	width, height = img.size #width and height of image

	for i in range(width):
		for j in range(height):
			r = region3x3(img, i, j)
			pixels[i, j] = avg(r)	

	return copyImage

def region3x3(img, x, y):
	img.load()
	list = [] 

	# Broken into rows
	list.append(getpixel(img, x-1, y-1))
	list.append(getpixel(img, x, y-1))
	list.append(getpixel(img, x+1, y-1))

	list.append(getpixel(img, x-1, y))
	list.append(getpixel(img, x, y))
	list.append(getpixel(img, x+1, y))

	list.append(getpixel(img, x-1, y+1))
	list.append(getpixel(img, x, y+1))
	list.append(getpixel(img, x+1, y+1)) 

	return list

def avg(data):
	return sum(data)/len(data)


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
			


if len(sys.argv)<=1:
	print "missing image filename"
	sys.exit(1)
filename = sys.argv[1]
img = Image.open(filename)
img = img.convert("L")
img.show()
img = blur(img)
img.show() # call your blur function

#img.show()
