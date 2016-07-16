import sys
from PIL import Image

def flip(img):
	imgCopy = img.copy() #copies the image
	flippedMatrix = imgCopy.load()  
	originalMatrix = img.load() #makes a matrix from an image
	width, height = img.size #width and height of image

	for i in range(height):
		j = width - 1
		k = 0
		while (j >= 0):
			flippedMatrix[k,i] = originalMatrix[j,i]
			j -= 1
			k += 1
	return imgCopy



if len(sys.argv)<=1:
	print "missing image filename"
	sys.exit(1)
filename = sys.argv[1]
img = Image.open(filename)
img = img.convert("L")
img.show()

img = flip(img) # call your flip function

img.show()
