import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('index.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
d=np.double(gray)
kernel = np.ones((3,3),np.float32)/9
m=np.log(d+1)
x=np.fft.fft2(m)
x=abs(x)
print x
print "\n"
for u in range(1,x.shape[0]-1):
    for v in range(1,x.shape[1]-1):
        x[u,v]=x[u,v] % 255
print x
'''v=np.fft.fftshift(x)
v=abs(v)
dst = cv2.filter2D(v,-1,kernel)
g1=(abs(np.fft.ifft2(dst)))
g=np.exp(g1)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(g),plt.title('homo')
plt.xticks([]), plt.yticks([])
plt.show()'''

