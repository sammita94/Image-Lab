import cv2
img = cv2.imread("Screenshot from 2016-08-24 15:45:22.png",0)
img2=img
for i in range(0,img2.shape[0]): 
    for j in range(0,img2.shape[1]):
	if(255-img2[i,j])<0:
		img2[i,j]=0
	else:
		img2[i,j]=255-img2[i,j]

cv2.imshow('window',img2)
cv2.waitKey(0);
cv2.destroyallwindows();
