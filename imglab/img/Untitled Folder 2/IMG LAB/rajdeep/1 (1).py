import cv2
import numpy as np
im = cv2.imread('blurred1.jpg'); #// Save image to computer first
xVals1 =np.array([1.,0.,-1.,2.,0,-2.,1.,0,-1.]).reshape(3,3)
yVals2 =np.array([-1.,-2.,-1.,0,0,0,1.,2.,1.]).reshape(3,3)

out1 = cv2.filter2D(im, cv2.CV_32F, xVals1, None, (-1,-1), 0, cv2.BORDER_DEFAULT)
out1 = cv2.convertScaleAbs(out1.copy())

out2 = cv2.filter2D(im, cv2.CV_32F, None, yVals2, (-1,-1), 0, cv2.BORDER_DEFAULT)
out2 = cv2.convertScaleAbs(out2.copy())

cv2.imshow('Sobel X-Axis', out1)
cv2.imshow('Sobel Y-Axis', out2)

cv2.waitKey(0)
cv2.destroyAllWindows()
