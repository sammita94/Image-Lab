import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('orinial.jpg',0)

img_float32 = np.double(img)
img_log = np.double(img)
img_exp = np.double(img)

rows, cols = img.shape
for i in range(rows):
	for j in range(cols):
		img_log[i,j] = np.log(1+img_float32[i,j])


dft = cv2.dft(img_log, flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)


crow, ccol = rows/2 , cols/2     # center

# create a mask first, center square is 1, remaining all zeros
mask = np.zeros((rows, cols, 2), np.uint8)
mask[crow-5:crow+5, ccol-5:ccol+5] = 1



# apply mask and inverse DFT
fshift = dft_shift*mask
f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])

for i in range(rows):
	for j in range(cols):
		img_exp[i,j] = np.exp(img_back[i,j])


plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_exp, cmap = 'gray')
plt.title('Homomorphic with lpf'), plt.xticks([]), plt.yticks([])

plt.show()
