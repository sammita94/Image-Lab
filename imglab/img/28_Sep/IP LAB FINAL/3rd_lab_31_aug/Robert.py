import cv2
import matplotlib
img = cv2.imread("soltandpepar2.png",1)
img2 = img
height, width, channels = img.shape
#print height, width
for i in range(0,height):
	for j in range(0,width):
		sum = 0
		if (i > 0 and j > 0):
			sum += -1*img[i-1,j-1]
		if (j > 0):
			sum += -1*img[i,j-1]

		if (i < height-1  and j > 0):
			sum += -1*img[i+1,j-1]
		if (i > 0):
			sum += 0*img[i-1,j]
		if (i < height-1):
			sum += 0*img[i+1,j]
		if (i > 0 and j < width-1):
			sum += 1*img[i-1,j+1]
		if (i > 0 and j < width-1):
			sum += 1*img[i,j+1]
		if (i < height-1 and j < width-1):
			sum += 1*img[i+1,j+1]
		img2[i,j] = sum


cv2.imshow('window',img2)
print img
print img2
cv2.waitKey(0)
