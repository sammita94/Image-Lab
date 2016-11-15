import cv2
from matplotlib import pyplot as plt
img = cv2.imread('sp2.png') 

#Median blurring
medBlur = cv2.medianBlur(img,5)
#cv2.imshow('Median Blurring', medBlur)
#cv2.waitKey(0)

plt.subplot(2,1,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,1,2),plt.imshow(medBlur,cmap = 'gray')
plt.title('Median'), plt.xticks([]), plt.yticks([])
plt.show()
#cv2.destroyAllWindows()
