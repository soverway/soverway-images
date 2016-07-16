from filter import *
# define function laplace here ...

def laplace(data):
	north = data[1]
	east = data[5]
	south = data[7]
	west = data[3]
	middle = data[4]

	return north + east + south + west - 4*middle

img = open(sys.argv)
img.show()
edges = filter(img, laplace)
edges.show()