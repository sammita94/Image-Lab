"""Code for Discrete Fourier Transform using numpy functions
"""


import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('fft.jpg',0)

#Fourier Transform 
f = np.fft.fft2(img)

#Shifting the DC component from top left to center
fshift = np.fft.fftshift(f)

#Finding the Magnitude Spectrum
magnitude_spectrum = 20*np.log(np.abs(fshift))

#Shifting the DC component back to the top left corner
f_ishift = np.fft.ifftshift(fshift)

#Inverse Fourier Transform 
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])

plt.subplot(132),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])

plt.subplot(133),plt.imshow(img_back, cmap = 'gray')
plt.title('Image inverted'), plt.xticks([]), plt.yticks([])

plt.show()
