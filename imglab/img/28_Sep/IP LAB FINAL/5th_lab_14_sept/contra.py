import cv2
import numpy as np
from matplotlib import pyplot as plt

source = cv2.imread("speckle.jpg", 0)
cv2.imshow('Source_Picture', source)

final = source[:]
sumi = 0;
sqsum=0;

for y in range(1,source.shape[0]-1):
    for x in range(1,source.shape[1]-1):
        final[y,x]=source[y,x]

members=[source[0,0]]*9  
sqmembers=[source[0,0]]*9 

for y in range(1,source.shape[0]-1):
    for x in range(1,source.shape[1]-1):
        sumi=0;
        sqsum=0;
        members[0] = (int)(source[y-1,x-1])
        sqmembers[0]=(int)((members[0]*members[0])%255)
        members[1] = (int)(source[y,x-1])
        sqmembers[1]=(int)((members[1]*members[1])%255)
        members[2] = (int)(source[y+1,x-1])
        sqmembers[2]=(int)((members[2]*members[2])%255)
        members[3] = (int)(source[y-1,x])
        sqmembers[3]=(int)((members[3]*members[3])%255)
        members[4] = (int)(source[y,x])
        sqmembers[4]=(int)((members[4]*members[4])%255)
        members[5] = (int)(source[y+1,x])
        sqmembers[5]=(int)((members[5]*members[5])%255)
        members[6] = (int)(source[y-1,x+1])
        sqmembers[6]=(int)((members[6]*members[6])%255)
        members[7] = (int)(source[y,x+1])
        sqmembers[7]=(int)((members[7]*members[7])%255)
        members[8] = (int)(source[y+1,x+1])
        sqmembers[8]=(int)((members[8]*members[8])%255)
        sumi=members[0]+members[1]+members[2]+members[3]+members[4]+members[5]+members[6]+members[7]+members[8]
        sqsum=sqmembers[0]+sqmembers[1]+sqmembers[2]+sqmembers[3]+sqmembers[4]+sqmembers[5]+sqmembers[6]+sqmembers[7]+sqmembers[8]
	if sumi == 0 :
             sumi = 1 
    	final[y,x]=(int)(sqsum/sumi)


cv2.imshow('Contra', final)
cv2.waitKey(0)


