from filter import *
# Your median function goes here (copy from denoise.py) ...

def median(data):
	sortedList = sorted(data)
	midpoint = len(sortedList)/2

	return sortedList[midpoint]


img = open(sys.argv)
img.show()
img = filter(img, median)
img.show()