"""Code for Discrete Fourier Transform
"""


import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('fft.jpg',0)

#1.Using numpy 
#f = np.fft.fft2(img)
#2.Using opencv2 package
f = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)

#Shifting the DC component from top left to center
fshift = np.fft.fftshift(f)

#Finding the Magnitude Spectrum
magnitude_spectrum = 20*np.log(np.abs(fshift))

#Shifting the DC component back to the top left corner
f_ishift = np.fft.ifftshift(fshift)

#Inverse Fourier Transform
#1.Using Numpy package 
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)


'''plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])

plt.subplot(132),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])'''

plt.subplot(133),plt.imshow(img_back, cmap = 'gray')
plt.title('Image inverted after Fourier Transform'), plt.xticks([]), plt.yticks([])

plt.show()
