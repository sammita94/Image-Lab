import cv2
from matplotlib import pyplot as plt

img = cv2.imread('soltpepar1.png') 

#Averaging
avg = cv2.blur(img,(10,10)) 
#cv2.imshow('mean',avg)
#cv2.waitKey(0)

#cv2.destroyAllWindows()

plt.subplot(2,1,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,1,2),plt.imshow(avg,cmap = 'gray')
plt.title('Mean'), plt.xticks([]), plt.yticks([])
plt.show()
