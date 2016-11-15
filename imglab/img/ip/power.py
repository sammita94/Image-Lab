import cv2
import numpy as np
import math

img = cv2.imread('img1.jpg',0)
cv2.imshow('window',img)

print img

img1 = img**2
cv2.imshow('window',img1)

cv2.waitKey(0)
