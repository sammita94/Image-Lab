import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('boundary2.JPG',0)
size = np.size(img)
skel = np.zeros(img.shape,np.uint8)
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
 
ret,img = cv2.threshold(img,127,255,0)
element = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
done = False
 
while( not done):
    eroded = cv2.erode(img,element)
    temp = cv2.dilate(eroded,element)
    temp = cv2.dilate(temp,element)
    temp = cv2.dilate(temp,element)
    skel = cv2.bitwise_or(skel,temp)
    img = eroded.copy()
 
    zeros = size - cv2.countNonZero(img)
    if zeros==size:
        done = True

plt.subplot(122),plt.imshow(skel, cmap = 'gray')
plt.title('Thickening'), plt.xticks([]), plt.yticks([])

plt.show()
