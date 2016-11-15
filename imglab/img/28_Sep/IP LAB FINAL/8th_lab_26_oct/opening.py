import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('OPENING CLOSING.JPG',0)
kernel = np.ones((5,5),np.uint8)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(opening, cmap = 'gray')
plt.title('Opening'), plt.xticks([]), plt.yticks([])

plt.show()
