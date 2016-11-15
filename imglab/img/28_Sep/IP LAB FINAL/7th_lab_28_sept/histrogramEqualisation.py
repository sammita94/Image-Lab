import cv2
import numpy as np
from matplotlib import pyplot as plt
	
img = cv2.imread('gaussian 1.png',0)
equ1 = cv2.equalizeHist(img)
equ2 = cv2.equalizeHist(equ1)

res = np.hstack((img,equ1, equ2))

#cv2.imwrite('res.png',res)
cv2.imshow('hist EQ', res)
cv2.waitKey(0)
