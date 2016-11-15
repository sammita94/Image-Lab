import cv2
import numpy as np
from matplotlib import pyplot as plt

source = cv2.imread("speckle.jpg", 0)
cv2.imshow('Source_Picture', source)

final = source[:]

for y in range(1,source.shape[0]-1):
    for x in range(1,source.shape[1]-1):
        final[y,x]=source[y,x]

members=[source[0,0]]*9  

for y in range(1,source.shape[0]-1):
    for x in range(1,source.shape[1]-1):
        members[0] = source[y-1,x-1]
        members[1] = source[y,x-1]
        members[2] = source[y+1,x-1]
        members[3] = source[y-1,x]
        members[4] = source[y,x]
        members[5] = source[y+1,x]
        members[6] = source[y-1,x+1]
        members[7] = source[y,x+1]
        members[8] = source[y+1,x+1]

    	members.sort()
    	final[y,x]=(members[0]+members[8])/2

cv2.imshow('Final_Picture', final)
cv2.waitKey(0)


