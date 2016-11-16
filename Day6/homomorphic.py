import cv2 # For OpenCV modules (For Image I/O and Contour Finding)
import numpy as np # For general purpose array manipulation
from matplotlib import pyplot as plt
import math

#### Main program

# Read in image
img = cv2.imread('screenshot.jpg', 0)

# Number of rows and columns
rows,cols = img.shape

# Convert image to 0 to 1, then do log(1 + I)
imgLog = np.log1p(np.array(img, dtype="float") / 255)

# Create Gaussian mask of sigma = 10
M = 2*rows + 1
N = 2*cols + 1
sigma = 10
(X,Y) = np.meshgrid(np.linspace(0,N-1,N), np.linspace(0,M-1,M))
centerX = np.ceil(N/2)
centerY = np.ceil(M/2)
gaussianNumerator = (X - centerX)**2 + (Y - centerY)**2

# Low pass and high pass filters
Hlow = np.exp(-gaussianNumerator / (2*sigma*sigma))
Hhigh = 1 - Hlow

# Move origin of filters so that it's at the top left corner to
# match with the input image
HlowShift = np.fft.ifftshift(Hlow.copy())
HhighShift = np.fft.ifftshift(Hhigh.copy())

# Filter the image and crop
img_f = np.fft.fft2(imgLog.copy(),(M,N))
Ioutlow = np.abs(np.fft.ifft2(img_f.copy() * HlowShift))
Iouthigh = np.abs(np.fft.ifft2(img_f.copy() * HhighShift))



 #Set scaling factors and add
gamma1 = 0.95
gamma2 = 1.05
Iout = gamma1*Ioutlow[0:rows,0:cols] + gamma2*Iouthigh[0:rows,0:cols]


Ihmf = np.expm1(Iout)
Ihmf2 = np.array(255*Ihmf, dtype="uint8")



cv2.imshow('Original Image', img)
cv2.imshow('Homomorphic Filtered Result', Ihmf2)
cv2.waitKey(0)
cv2.destroyAllWindows()
