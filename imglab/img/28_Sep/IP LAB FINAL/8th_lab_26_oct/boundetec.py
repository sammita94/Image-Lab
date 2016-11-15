import cv2
import numpy as np
from matplotlib import pyplot as plt

# loading image
#img0 = cv2.imread('SanFrancisco.jpg',)
img = cv2.imread('Boundary.JPG',)
plt.subplot(1,3,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

# converting to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# remove noise
img = cv2.GaussianBlur(gray,(3,3),0)

# convolute with proper kernels
#laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)  # x
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)  # y

plt.subplot(1,3,2),plt.imshow(sobelx+sobely,cmap = 'gray')
plt.title('First Order Diff'), plt.xticks([]), plt.yticks([])

kernel = np.ones((5,5),np.uint8)
bound = cv2.erode(sobelx+sobely,kernel,iterations = 1)
bound = sobelx+sobely-bound



plt.subplot(1,3,3),plt.imshow(bound,cmap = 'gray')
plt.title('Boundary'), plt.xticks([]), plt.yticks([])


plt.show()
