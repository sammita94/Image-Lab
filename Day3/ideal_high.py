'''Ideal High Pass 
'''


import numpy as np
import cv2
from matplotlib import pyplot as plt


img = cv2.imread('fft.jpg',0)

#Fourier Transform
dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)

#Shifting the DC component to the center
dft_shift = np.fft.fftshift(dft)

rows, cols = img.shape
crow,ccol = rows/2 , cols/2

# create a mask first, center square is 0, remaining all ones
mask = np.ones((rows,cols,2),np.uint8)
mask[crow-30:crow+30, ccol-30:ccol+30] = 0

# apply mask and inverse DFT
fshift = dft_shift*mask

#Shifting DC component back to top left corner
fshift = np.fft.ifftshift(fshift)

#Inverse Fourier Transform
img_back = cv2.idft(fshift)
img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_back, cmap = 'gray')
plt.title('Inverted image'), plt.xticks([]), plt.yticks([])

plt.show()