import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('b22.jpg',0)

img2= cv2.imread('l2.jpg',0)
##   img = cv2.imread('home.jpg',0)
##hist1 = plt.hist(img1.ravel(),256,[0,256]); plt.show()
##hist2 = plt.hist(img2.ravel(),256,[0,256]); plt.show()

equ1 = cv2.equalizeHist(img1)
##res1 = np.hstack((img1,equ))

equ2 = cv2.equalizeHist(img2)
##res2 = np.hstack((img2,equ))

histadd = equ1+equ2
histsub = equ1-equ2
##print hist1, hist2
cv2.imshow('AddH', histadd)
cv2.imshow('SubH', histsub)
cv2.imshow('Add', img1+img2)
cv2.imshow('Sub', img1-img2)
cv2.waitKey(0)
