import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('index.jpg',0)

img_eq = cv2.equalizeHist(img)

cv2.imshow('Input image', img)

cv2.imshow('Histogram equalized picture', img_eq)

plt.hist(img.ravel(),256,[0,256])
plt.title('Histogram for input picture')
plt.show()

plt.hist(img_eq.ravel(),256,[0,256])
plt.title('Histogram for equalized picture')
plt.show()


cv2.waitKey(0)
