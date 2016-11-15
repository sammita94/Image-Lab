import cv2
from matplotlib import pyplot as plt
ksize = 1
scale = 1
delta = 0
ddepth = cv2.CV_16S

img = cv2.imread('gaussian2.jpg')
out1 = cv2.GaussianBlur(img,(3,3),0)

img2 = cv2.imread('gaussian 1.png')
out2 = cv2.GaussianBlur(img2,(3,3),0)

plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original1'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(out1,cmap = 'gray')
plt.title('Gaussian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(img2,cmap = 'gray')
plt.title('Original2'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(out2,cmap = 'gray')
plt.title('Gaussian 2'), plt.xticks([]), plt.yticks([])

plt.show()









