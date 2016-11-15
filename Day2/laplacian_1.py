import cv2
import numpy as np

 

gs_imagem = cv2.imread("index.jpg",0)
cv2.imshow("Original",gs_imagem) 

xVals =np.array([1.,1.,1.,1.,-8.,1.,1.,1.,1.]).reshape(3,3)
yVals =np.array([-1.,-1.,-1.,-1.,8.,-1.,-1.,-1.,-1.]).reshape(3,3)

out1 = cv2.filter2D(gs_imagem, cv2.CV_32F, xVals, yVals, (-1,-1), 0, cv2.BORDER_DEFAULT)
out1 = cv2.convertScaleAbs(out1.copy())

cv2.imshow('Laplacian Filter', out1)
cv2.waitKey(0)

