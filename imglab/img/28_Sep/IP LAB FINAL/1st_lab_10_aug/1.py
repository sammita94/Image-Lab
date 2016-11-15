#first lab program
import cv2
import matplotlib
#0-gray, 1-original, -1=color
img1 = cv2.imread("BW.png",1)
cv2.imshow('xxx', img1)
cv2.waitKey(0)
