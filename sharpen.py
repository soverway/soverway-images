from filter import *
# define function laplace here ...

def laplace(data):
	north = data[1]
	east = data[5]
	south = data[7]
	west = data[3]
	middle = data[4]

	return north + east + south + west - 4*middle

def minus(A, B):
	Apixels = A.load()
	Bpixels = B.load()
	width, height = A.size #width and height of image

	for i in range(width):
		for j in range(height):
			Apixels[i, j] -= Bpixels[i, j]
	return A		

img = open(sys.argv)
img.show()
edges = filter(img, laplace)
minusImage = minus(img, edges)
minusImage.show()