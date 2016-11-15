import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('OPENING CLOSING.JPG',0)
kernel = np.ones((5,5),np.uint8)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(closing, cmap = 'gray')
plt.title('Closing'), plt.xticks([]), plt.yticks([])

plt.show()
