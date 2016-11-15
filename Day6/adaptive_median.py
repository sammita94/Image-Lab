import cv2
import numpy as np
from matplotlib import pyplot as plt
import math


smax = 9

source = cv2.imread('img.png',0)
cv2.imshow('Input image',source)

final = source

rows,cols = source.shape

ll = int(math.ceil(float(float(smax)/2)))
ul = int(math.floor(float(float(smax)/2)))

for y in range(ll,rows-ul):
	for x in range(ll,cols-ul):
		center = source[y][x]
		win_size = 3
		while win_size <= smax:
		    members = np.empty(win_size**2 + 1, dtype=int)
	            k = 0
	            index = (win_size-1)/2
                    for i in range(-index,index+1):
	                for j in range(-index,index+1):
			    members[k]=source[y+i][x+j]
			    k = k+1
	            members.sort()
	            rmin = members[0]
	            rmax = members[(win_size*win_size)-1]
	            rmed = members[(win_size*win_size)/2]
                    if (rmed < rmax) and (rmed > rmin):
			if(center >= rmax) or (center <= rmin):
			    final[y][x]= rmed
			else:
			    final[y][x] = center
			break
		    else:
		        if win_size==smax:
		            final[y][x]= center

                    win_size = win_size+2



cv2.imshow('Output image',final)
cv2.waitKey(0)


