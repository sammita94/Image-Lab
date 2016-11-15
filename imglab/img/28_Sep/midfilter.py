import cv2
import numpy
import matplotlib
img = cv2.imread("gaussian.jpg",0)
img2 = cv2.imread("gaussian.jpg",0)
height, width = img.shape
print height, width
for i in range(0, height):
	for j in range(0, width):
		min = img[i,j]
		max = img[i,j]	
		if (i > 0 and j > 0 and img[i-1,j-1] > max):
			max = img[i-1,j-1]
		if (i > 0 and j > 0 and img[i-1,j-1] < min):
			min = img[i-1,j-1]				
		if (j > 0 and img[i,j-1] > max):
			max = img[i,j-1]
		if (j > 0 and img[i,j-1] < min):
			min = img[i,j-1]
		if (i < height-1  and j > 0 and img[i+1,j-1] > max):
			max = img[i+1,j-1]	
		if (i < height-1  and j > 0 and img[i+1,j-1] < min):
			min = img[i+1, j - 1]
		if (i > 0 and img[i-1,j] > max):
			max = img[i-1,j]
		if (i > 0 and img[i-1,j] < min):
			min = img[i-1,j]	
		if (i < height-1 and img[i+1,j] > max):
			max = img[i+1,j]	
		if (i < height-1 and img[i+1,j] < min):
			min = img[i+1,j]
		if (i > 0 and j < width-1 and img[i-1,j+1] > max):
			max = img[i-1,j+1]
		if (i > 0 and j < width-1 and img[i-1,j+1] < min):
			min = img[i-1,j+1]	
		if (i > 0 and j < width-1 and img[i,j+1] > max):
			max = img[i,j+1]	
		if (i > 0 and j < width-1 and img[i,j+1] < min):
			min = img[i,j+1]
		if (i < height-1 and j < width-1 and img[i+1,j+1] > max):
			max = img[i+1,j+1]	
		if (i < height-1 and j < width-1 and img[i+1,j+1] < min):
			min = img[i+1,j+1]	
		img2[i,j] = min + (max-min)/2
cv2.imshow('window1',img)	
cv2.imshow('window2',img2)
#print img2
#print img
cv2.waitKey(0)					
					

