import cv2
import numpy as np
from matplotlib import pyplot as plt
import math
a=cv2.imread('DCT.PNG')
r1 = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
row=len(r1)
col=len(r1[0])
b=r1
H = a[:]
v1=a
g=a
g1=a
'''D0=input('enter cut off : ')
Yh=input('enter the value of Yh :');
Yl=input('enter the value of Yl :');
C=input('enter the value of c :');'''
D0=25
Yh=50
Yl=50
C=4
for x in range(1,row):
    for y in range(1,col):
        if (r1[x,y]==0) :
            b[x,y]=1
        
   
for u in range(1,row):
      for v in range(1,col):
       	 D=int(int(int(u-int(row/2))^2+int(v-int(col/2))^2)^1)
         H[u,v]=int((Yh-Yl)*(1-math.exp(-C*(D*D/D0*D0)))+Yl)
      
  
m=np.log(b)
x=np.fft.fft2(m)
v=np.fft.fftshift(x)
for u in range(1,row):
      for v in range(1,col):
       	 v1=H[u,v]*v
	 g1=255-v1	
#g=np.exp(g1)
#figure(1)
cv2.imshow(g1)
#figure(2)
cv2.imshow(r1)
