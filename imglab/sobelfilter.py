import cv2
import numpy as np
from matplotlib import pyplot as plt

# loading image

img0 = cv2.imread('gaussian 1.png')

# converting to gray scale
gray = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)

# remove noise
#img = cv2.GaussianBlur(gray,(3,3),0)


sobelx = cv2.Sobel(img0,cv2.CV_64F,1,0,ksize=3)  # x
sobely = cv2.Sobel(img0,cv2.CV_64F,0,1,ksize=3)  # y

plt.subplot(2,2,1),plt.imshow(img0,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,2),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel horizontal'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobely,cmap = 'gray')  
plt.title('Sobel vertical'), plt.xticks([]), plt.yticks([])

plt.show()

