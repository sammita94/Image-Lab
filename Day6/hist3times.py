import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('index.jpg',0)

eq1 = cv2.equalizeHist(img)
cv2.imshow('Histogram 1 pass', eq1)

eq2 = cv2.equalizeHist(eq1)
cv2.imshow('Histogram 2 pass', eq2)

eq3 = cv2.equalizeHist(eq2)
cv2.imshow('Histogram 3 pass', eq3)

cv2.waitKey(0)
