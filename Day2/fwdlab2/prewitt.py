import cv2
import numpy as np
im = cv2.imread('blurred1.jpg'); #// Save image to computer first

#// Call using built-in Sobel
#out1 = cv2.Sobel(im, cv2.CV_16S, 0, 1, 3)
#out1 = cv2.convertScaleAbs(out1.copy())

#// Create custom kernel
xVals =np.array([-1.,0.,1.,-1.,0,1.,-1.,0,1.]).reshape(3,3)
yVals =np.array([-1.,-1.,-1.,0,0,0,1.,1.,1.]).reshape(3,3)

#// Call filter2D
out2 = cv2.filter2D(im, cv2.CV_32F, xVals, yVals, (-1,-1), 0, cv2.BORDER_DEFAULT)
out2 = cv2.convertScaleAbs(out2.copy())

#cv2.imshow('Output 1', out1)
cv2.imshow('Output 2', out2)
cv2.waitKey(0)
cv2.destroyAllWindows()
