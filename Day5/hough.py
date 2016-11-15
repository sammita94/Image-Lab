import numpy as np
import cv2
from matplotlib import pyplot as plt

#Making the image with noise points at the line having points (0,0), (1,1), (2,2) ,(3,3),(4,4)
img = np.zeros((258,258))
img = np.uint8(img)
for i in range(0,258):
	for j in range(0,258):
		if(i==j and i<110):
			img[i][j]=0
		else:
			img[i][j]=255


#Displaying input image
cv2.imshow('Input',img)
w, h = 100, 100 
lines = [[0 for x in range(w)] for y in range(h)] 

#Finding all edges in the image
edges = cv2.Canny(img,50,150,apertureSize = 3)

#Finding all lines in the image with votes greater than or equal to 50 (Since only the one line exists, it will be the best detection)
lines = cv2.HoughLines(edges,1,np.pi/180,100)


for rho,theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imshow('Output', img)
cv2.waitKey(0)
