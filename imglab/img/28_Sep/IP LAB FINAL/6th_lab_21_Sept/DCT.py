import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('nitdgp.jpg',0)

imf = np.float32(img)/255.0

dst = cv2.dct(imf)           # the dct
imgcv1 = np.uint8(dst)*255.0    # convert back

dstinv = cv2.idct(dst)           # inverse dct
imgcv2 = np.uint8(dstinv)*255.0    # convert back

plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(dst, cmap = 'gray')
plt.title('dst image'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(imgcv2, cmap = 'gray')
plt.title('convert back'), plt.xticks([]), plt.yticks([])
plt.show()       
