import cv2
import numpy as np
im = cv2.imread('saltpepar2.png'); #// Save image to computer first

#// Call using built-in Sobel
#out1 = cv2.Sobel(im, cv2.CV_16S, 0, 1, 3)
#out1 = cv2.convertScaleAbs(out1.copy())

#// Create custom kernel
xVals1 =np.array([1.,0,-1.,2.,0,-2.,1.,0,-1.]).reshape(3,3)
yVals2 =np.array([-1.,-2.,-1.,0,0,0,1.,2.,1.]).reshape(3,3)
xVals3 =np.array([-1.,0.,1.,-1.,0,1.,-1.,0,1.]).reshape(3,3)
yVals4 =np.array([-1.,-1.,-1.,0,0,0,1.,1.,1.]).reshape(3,3)
xVals5 =np.array([1.,0,0,-1.]).reshape(2,2)
yVals6 =np.array([0,1.,-1.,0]).reshape(2,2)
xVals7 =np.array([1.,1.,1.,1.,-8.,1.,1.,1.,1.]).reshape(3,3)
yVals8 =np.array([-1.,-1.,-1.,-1.,8.,-1.,-1.,-1.,-1.]).reshape(3,3)
xVals9 =np.array([0.11,0.11,0.11,0.11,0.11,0.11,0.11,0.11,0.11]).reshape(3,3)

#// Call filter2D
out1 = cv2.filter2D(im, cv2.CV_32F, xVals1, yVals2, (-1,-1), 0, cv2.BORDER_DEFAULT)
out1 = cv2.convertScaleAbs(out1.copy())

#out2 = cv2.filter2D(im, cv2.CV_32F, None, yVals2, (-1,-1), 0, cv2.BORDER_DEFAULT)
#out2 = cv2.convertScaleAbs(out2.copy())

out3= cv2.filter2D(im, cv2.CV_32F, xVals3, yVals4, (-1,-1), 0, cv2.BORDER_DEFAULT)
out3= cv2.convertScaleAbs(out3.copy())

#out4 = cv2.filter2D(im, cv2.CV_32F, None, yVals4, (-1,-1), 0, cv2.BORDER_DEFAULT)
#out4 = cv2.convertScaleAbs(out4.copy())

out5 = cv2.filter2D(im, cv2.CV_32F, xVals5, yVals6, (-1,-1), 0, cv2.BORDER_DEFAULT)
out5= cv2.convertScaleAbs(out5.copy())

#out6= cv2.filter2D(im, cv2.CV_32F, None, yVals6, (-1,-1), 0, cv2.BORDER_DEFAULT)
#out6= cv2.convertScaleAbs(out6.copy())

out7= cv2.filter2D(im, cv2.CV_32F, xVals7, yVals8, (-1,-1), 0, cv2.BORDER_DEFAULT)
out7= cv2.convertScaleAbs(out7.copy())

#out8= cv2.filter2D(im, cv2.CV_32F, None, yVals8, (-1,-1), 0, cv2.BORDER_DEFAULT)
#out8= cv2.convertScaleAbs(out8.copy())

out9= cv2.filter2D(im, cv2.CV_32F, xVals9,None, (-1,-1), 0, cv2.BORDER_DEFAULT)
out9= cv2.convertScaleAbs(out9.copy())

#cv2.imshow('Output 1', out1)
cv2.imshow('Sobel ', out1)
#cv2.imshow('Sobel Y-Axis', out2)
cv2.imshow('Prewitt ', out3)
#cv2.imshow('Prewitt Y-Axis', out4)
cv2.imshow('Robert ', out5)
#cv2.imshow('Robert Y-Axis', out6)
cv2.imshow('Laplacian ', out7)
cv2.imshow('Mean', out9)
#cv2.imshow('Laplacian Y-Axis', out8)
cv2.waitKey(0)
cv2.destroyAllWindows()
