
import cv2
import numpy as np

def logarithm(image, name):
    image=image+1
    cv2.log(image,image)
    cv2.normalize(image,image,0,255,cv2.NORM_MINMAX)
    cv2.convertScaleAbs(image,image)
   
    cv2.imwrite(name, image)

img = cv2.imread("img1.jpg",0)
img = np.float64(img)
logarithm(img, "output.png")
img1 = cv2.imread("output.png")
cv2.imshow("window",img1)
cv2.waitKey(0)

