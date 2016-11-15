"""python code to load a image using opencv
   @author Arpit and Sammita
   @Date :10/08/2016
"""

import cv2

im = cv2.imread("index.jpg",1)
cv2.imshow("Sample",im)
cv2.waitKey(10000)

