import cv2
import numpy as np
import math
from matplotlib import pyplot as plt


img = cv2.imread('index.jpg',0)

#Adding noise
source = img
rows, cols = img.shape
mean = 156
var = 156.1
sigma = var**0.5
gauss = np.random.normal(mean,sigma,(rows,cols))
gauss = gauss.reshape(rows,cols)
img = gauss + img

#Fourier Transform
dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)

#Shifting the DC component to the center
dft_shift = np.fft.fftshift(dft)


crow,ccol = rows/2 , cols/2

mask = np.zeros((rows, cols, 2))

for i in range(rows):
    for j in range(cols):
    	distance = float(((i-crow)**2 + (j-ccol)**2))
        mask[i,j] = math.exp(-0.0025*(float(distance**0.777)))
        #print mask[i,j]

# apply mask to degrade
fshift = dft_shift*mask

#Shifting DC component back to top left corner
fshift = np.fft.ifftshift(fshift)

#Inverse Fourier Transform
img_back = cv2.idft(fshift)
img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])

#Applying Inverse Filter

img_fil = img_back

#Fourier Transform
dft = cv2.dft(np.float32(img_fil),flags = cv2.DFT_COMPLEX_OUTPUT)

#Shifting the DC component to the center
dft_shift = np.fft.fftshift(dft)

rows, cols = img.shape
crow,ccol = rows/2 , cols/2

mask = np.zeros((rows, cols, 2))

for i in range(rows):
    for j in range(cols):
    	distance = float(((i-crow)**2 + (j-ccol)**2))
        mask[i,j] = math.exp(-0.0025*(float(distance**0.777)))
        #print mask[i,j]

# apply mask to degrade
fshift = dft_shift/mask

#Shifting DC component back to top left corner
fshift = np.fft.ifftshift(fshift)

#Inverse Fourier Transform
img_fil = cv2.idft(fshift)
img_fil = cv2.magnitude(img_fil[:,:,0],img_fil[:,:,1])

plt.subplot(131),plt.imshow(source, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(img_back, cmap = 'gray')
plt.title('Degraded image'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(img_fil, cmap = 'gray')
plt.title('Inverse filtered image'), plt.xticks([]), plt.yticks([])

plt.show()