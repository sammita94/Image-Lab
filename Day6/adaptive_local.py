import cv2
import numpy as np
from matplotlib import pyplot as plt

#Reading image
source = cv2.imread('gaussian.jpg',0)
cv2.imshow('Input image',source)
#
row,col= source.shape

noisy = source

for y in range(1,row-1):
    for x in range(1,col-1):
        noisy[y,x]=float (noisy[y,x])
m=5
n=5
row, col= noisy.shape[:2]
bottom= noisy[row-2:row, 0:col]
mean= cv2.mean(bottom)[0]

#Padding the image
bordersize=2
border=cv2.copyMakeBorder(noisy, top=bordersize, bottom=bordersize, left=bordersize, right=bordersize, borderType= cv2.BORDER_CONSTANT, value=[mean,mean,mean] )

mean_m=np.empty(shape=[row+4,col+4])
var_m=np.empty(shape=[row+4,col+4])


for y in range(1,noisy.shape[0]-1):
    for x in range(1,noisy.shape[1]-1):
        lm=0
        su=0
        sq=0
        lv=0
        for i in range(-1,2):
            for j in range(-1,2):
                su+=noisy[y+i][x+j]
		sq += (noisy[y+i][x+j])**2
	lm = su/9;
	lv = (sq/9)-lm**2
	mean_m[y][x] = lm
	var_m[y][x] = lv

count = 0
sv=0
for y in range(1,var_m.shape[0]-1):
    for x in range(1,var_m.shape[1]-1):
	su+=var_m[y][x]
	count+= 1

avg_v = su/count

for y in range(1,var_m.shape[0]-1):
    for x in range(1,var_m.shape[1]-1):
	if(var_m[y][x]<avg_v):
            var_m[y][x]=avg_v


for y in range(1,noisy.shape[0]-1):
    for x in range(1,noisy.shape[1]-1):
	noisy[y][x] = noisy[y][x] -(avg_v/var_m[y][x])*(noisy[y][x]-mean_m[y][x])

	
cv2.imshow('Final_Picture', noisy)
cv2.waitKey(0)

