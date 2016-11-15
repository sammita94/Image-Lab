import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('butterworth.png',0)

img_float32 = np.float32(img)

dft = cv2.dft(img_float32, flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

rows, cols = img.shape
crow, ccol = rows/2 , cols/2     # center

# create a mask first, center square is 1, remaining all zeros
mask = np.zeros((rows, cols, 2), np.uint8)

for i in range(crow):
	for j in range(ccol):
		mask[i,j] = int(np.exp((int(((i-crow)**(2) + (j-ccol)**(2)))**(0.5))**(2)/230**(2)))


for i in range(crow+1,rows):
	for j in range(ccol+1,cols):
		mask[i,j] = int(np.exp((int(((i-crow)**(2) + (j-ccol)**(2)))**(0.5))**(2)/230**(2)))



# apply mask and inverse DFT
fshift = dft_shift*mask
f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_back, cmap = 'gray')
plt.title('GaussianLow'), plt.xticks([]), plt.yticks([])

plt.show()
