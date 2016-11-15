import cv2
import numpy as np
from matplotlib import pyplot as plt
f = cv2.imread("speckle.jpg", 0)
cv2.imshow('Source_Picture', f)

b1 = f[:]
m,n = f.shape
si=1
Q=1
for i in range (1,m):
	for j in range (1,n):
                con=0; s1=0; s2=0;
		for k1 in range (i-si,i+si):
			for p1 in range (j-si,j+si):
				if ((k1>0 and p1 >0) and (k1<m and p1<n)):
					con = con+1
					s1=s1+(f[k1,p1]**Q)
					s2=s2+(f[k1,p1]**(Q+1))

		b1[i,j]=s2/s1;

cv2.imshow('Final_Picture', b1)
cv2.waitKey(0)
