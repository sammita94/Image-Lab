'''DFT using OpenCV functions
'''


import numpy as np
import cv2
from matplotlib import pyplot as plt


img = cv2.imread('fft.jpg',0)

#Fourier Transform
dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)

#Shifting the DC component to the center
dft_shift = np.fft.fftshift(dft)

#Magnitude Spectrum
magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))

#Shifting DC component back to top left corner
f_ishift = np.fft.ifftshift(dft_shift)

#Inverse Fourier Transform
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])

plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(img_back, cmap = 'gray')
plt.title('Inverted image'), plt.xticks([]), plt.yticks([])

plt.show()