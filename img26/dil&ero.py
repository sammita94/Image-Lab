import cv2
import cv
import numpy as np

img = cv2.imread('Erosion.JPG', 0)
img2 = cv2.imread('Dialation Input.JPG', 0)

kernel = np.ones((3,3), np.uint8)
kernel_ero = np.ones((3,3), np.uint8)
kernel_dil = kernel_ero


img_erosion = cv2.erode(img, kernel_ero, iterations=1)
img_dilation = cv2.dilate(img2, kernel_dil, iterations=1)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
#hitmiss = np.morphologyEx(img, cv.MORPH_HITMISS, kernel)

cv2.imshow('Input', img)
cv2.imshow('Erosion', img_erosion)
cv2.imshow('Dilation', img_dilation)
cv2.imshow('Opening', opening)
cv2.imshow('Closing', closing)
#cv2.imshow('Hit Miss', hitmiss)

cv2.waitKey(0)
