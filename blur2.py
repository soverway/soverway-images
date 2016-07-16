from filter import *


# Your avg function goes here (copy from blur.py) ...
def avg(data):
	return sum(data)/len(data)

img = open(sys.argv)
img.show()
img = filter(img, avg)
img.show()