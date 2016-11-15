import numpy as np
import cv2
from matplotlib import pyplot as plt
from numpy import empty,arange,exp,real,imag,pi
from numpy.fft import rfft,irfft
# 1D DST Type-I

def dst(y):
    N = len(y)
    y2 = empty(2*N,float)
    y2[0] = y2[N] = 0.0
    y2[1:N] = y[1:]
    y2[:N:-1] = -y[1:]
    a = -imag(rfft(y2))[:N]
    a[0] = 0.0

    return a


######################################################################
# 1D inverse DST Type-I

def idst(a):
    N = len(a)
    c = empty(N+1,complex)
    c[0] = c[N] = 0.0
    c[1:N] = -1j*a[1:]
    y = irfft(c)[:N]
    y[0] = 0.0

    return y


######################################################################
# 2D DST

def dst2(y):
    M = y.shape[0]
    N = y.shape[1]
    a = empty([M,N],float)
    b = empty([M,N],float)

    for i in range(M):
        a[i,:] = dst(y[i,:])
    for j in range(N):
        b[:,j] = dst(a[:,j])

    return b


######################################################################
# 2D inverse DST

def idst2(b):
    M = b.shape[0]
    N = b.shape[1]
    a = empty([M,N],float)
    y = empty([M,N],float)

    for i in range(M):
        a[i,:] = idst(b[i,:])
    for j in range(N):
        y[:,j] = idst(a[:,j])

    return y

img = cv2.imread('nitdgp.jpg',0)
cv2.imshow('image1',img)
imf = np.float32(img)
dcti = dst2(imf) 
imgcv0 = np.uint8(dcti) 
dctii = idst2(dcti)
imgcv1 = np.uint8(dctii)

cv2.imshow('image2',imgcv)
cv2.waitKey(0)

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dcti, cmap = 'gray')
plt.title('dst image'), plt.xticks([]), plt.yticks([])
#plt.show()
