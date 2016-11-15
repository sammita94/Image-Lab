import cv2
import numpy as np
import math
from matplotlib import pyplot as plt

img=cv2.imread('/home/imag_lab2/img.png',0)
img2=img
for i in range(0,img2.shape[0]):
    for j in range(0,img2.shape[1]):
	img2[i,j]=-img2[i,j]
cv2.imshow("inverse",img2)
cv2.waitKey(0)

