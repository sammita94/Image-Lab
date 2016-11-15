import cv2
import numpy as np
img = cv2.imread( 'img1.jpg', 0 )
cv2.imshow('window',img)
print img
print 255-img
img1  = 255-img;
cv2.imshow('window', img1)
cv2.waitKey(0)

