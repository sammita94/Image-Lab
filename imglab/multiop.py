import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('index.jpg')
img2 = cv2.imread('gaussian.jpg')

#img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

# equalize the histogram of the Y channel
#img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])

# convert the YUV image back to RGB format
#img_output = cv2.cvtColor(img_yuv, cv2.COLOR_BGR2GRAY)

img3 = img1+img2
img4 = img1-img2


cv2.imshow('Color input image2', img3)
cv2.imshow('Color input image3', img4)
"""cv2.imshow('Histogram equalized', img_output)
plt.hist(img_output.ravel(),256,[0,256])
plt.title('Histogram for gray scale picture')
plt.show()"""

cv2.waitKey(0)
