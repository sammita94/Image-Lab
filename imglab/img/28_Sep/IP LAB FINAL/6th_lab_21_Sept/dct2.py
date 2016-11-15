import numpy as np
import cv2
from matplotlib import pyplot as plt
from numpy import empty,arange,exp,real,imag,pi
from numpy.fft import rfft,irfft

def idct(a):
    N = len(a)
    c = empty(N+1,complex)

    phi = exp(1j*pi*arange(N)/(2*N))
    c[:N] = phi*a
    c[N] = 0.0
    return irfft(c)[:N]

def idct2(b):
    M = b.shape[0]
    N = b.shape[1]
    a = empty([M,N],float)
    y = empty([M,N],float)

    for i in range(M):
        a[i,:] = idct(b[i,:])
    for j in range(N):
        y[:,j] = idct(a[:,j])

    return y

def dct(y):
    N = len(y)
    y2 = empty(2*N,float)
    y2[:N] = y[:]
    y2[N:] = y[::-1]

    c = rfft(y2)
    phi = exp(-1j*pi*arange(N)/(2*N))
    return real(phi*c[:N])


def dct2(y):
    M = y.shape[0]
    N = y.shape[1]
    a = empty([M,N],float)
    b = empty([M,N],float)

    for i in range(M):
        a[i,:] = dct(y[i,:])
    for j in range(N):
        b[:,j] = dct(a[:,j])

    return b

img = cv2.imread('nitdgp.jpg',0)
cv2.imshow('image1',img)
imf = np.float32(img)
dcti = dct2(imf)  
dctii = idct2(dcti)
imgcv1 = np.uint8(dctii)


cv2.imshow('image2',imgcv1)
cv2.waitKey(0)

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dcti, cmap = 'gray')
plt.title('dct image'), plt.xticks([]), plt.yticks([])
#plt.show()

