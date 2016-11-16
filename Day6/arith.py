import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('b1.jpg',0)
img2= cv2.imread('b2.jpg',0)

hist1 = cv2.calcHist([img1],[0],None,[256],[0,256])
hist2 = cv2.calcHist([img2],[0],None,[256],[0,256])

#imgadd = cv2.add(img1,img2)
#imgsub = cv2.sub(img1,img2)

histadd = hist1+hist2
histsub = hist1-hist2


cv2.imshow('Add', img1+img2)
cv2.imshow('Sub', img1-img2)

plt.subplot(141),plt.plot(hist1),plt.title('Img1')
plt.xlim([0,256])
plt.subplot(142),plt.plot(hist2),plt.title('Img2')
plt.xlim([0,256])
plt.subplot(143),plt.plot(histadd),plt.title('Add')
plt.xlim([0,256])
plt.subplot(144),plt.plot(histsub),plt.title('Sub')
plt.xlim([0,256])
plt.show()
cv2.waitKey(0)

