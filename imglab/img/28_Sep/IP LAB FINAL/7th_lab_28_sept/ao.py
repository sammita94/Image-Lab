import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('gaussian 1.png',0)

img2= cv2.imread('gaussian 2.png',0)

imga = int(img1 + img2)
cv2.imshow('Arithemetic Operations', imga)
cv2.waitKey(0)
