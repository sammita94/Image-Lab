import cv2
import numpy as np
from matplotlib import pyplot as plt
source = cv2.imread("gaussian.jpg", 0)
cv2.imshow('Source_Picture', source)

final = source
rows,cols = source.shape

Q=1

for y in range (1,rows):
	for x in range (1,cols):
                s1=0; s2=0;
		for k1 in range (y-1,y+2):
			for p1 in range (x-1,x+2):
				if ((k1>0 and p1 >0) and (k1<rows and p1<cols)):
					s1=s1+(f[k1,p1]**Q)
					s2=s2+(f[k1,p1]**(Q+1))

		final[y,x]=s2/s1;

cv2.imshow('Final_Picture', final)
cv2.waitKey(0)
