import cv2
import numpy as np
from matplotlib import pyplot as plt

#Read image
source = cv2.imread("gaussian.jpg", 0)
cv2.imshow('Source_Picture', source)

final = source[:]
rows,cols = source.shape

for y in range(1,rows-1):
    for x in range(1,cols-1):
        final[y,x]=source[y,x]

members=[source[0,0]]*9  

#Sort all 8 neighbours and then formula and take weighted average
alpha = 0.5
for y in range(1,source.shape[0]-1):
    for x in range(1,source.shape[1]-1):
        co = 0
        for k1 in range (y-1,y+2):
            for p1 in range (x-1,x+2):
                if ((k1>0 and p1 >0) and (k1<rows and p1<cols)):
                    members[co]=source[k1][p1]
                    co = co+1
        members.sort()
        final[y,x]=((alpha)*members[0]+(1-alpha)*(members[8]))

cv2.imshow('Final_Picture', final)
cv2.waitKey(0)


