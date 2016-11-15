import cv2
import numpy as np

 

gs_imagem = cv2.imread("Bikesgray.jpg",0)
cv2.imshow("Original",gs_imagem) 

xVals =np.array([1.,0,-1.,2.,0,-2.,1.,0,-1.]).reshape(3,3)
yVals =np.array([-1.,-2.,-1.,0,0,0,1.,2.,1.]).reshape(3,3)

out3 = cv2.filter2D(gs_imagem, cv2.CV_32F, xVals, yVals, (-1,-1), 0, cv2.BORDER_DEFAULT)
out1 = cv2.filter2D(gs_imagem, -1 , xVals)
out2 = cv2.filter2D(gs_imagem, -1 , yVals)

out3 = cv2.convertScaleAbs(out3.copy())

cv2.imshow('Sobel X Filter', out1)
cv2.imshow('Sobel Y Filter', out2)
cv2.imshow('Sobel Normalized Filter', out3)
cv2.waitKey(0)


