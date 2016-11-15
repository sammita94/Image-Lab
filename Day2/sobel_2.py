import cv2
import numpy as np

gs_imagem = cv2.imread("Bikesgray.jpg",0)
cv2.imshow("Original",gs_imagem) 

xVals =np.array([1.,0,-1.,2.,0,-2.,1.,0,-1.]).reshape(3,3)
yVals =np.array([-1.,-2.,-1.,0,0,0,1.,2.,1.]).reshape(3,3)

row,col = gs_imagem.shape

sobel_x = gs_imagem
sobel_y = gs_imagem
sobel_whole = gs_imagem

for i in range(0,row):
    for j in range(0,col):
        summ = 0
        count = 0
        if i == 0 or j == 0 or i == row-1 or j == col-1 :
        	continue
        else:
    	    for i_w in range(-1,2):
    	        for j_w in range(-1,2):
    		    ii = i + i_w
    		    jj = j + j_w
    		    i_f = 1 + i_w
    		    j_f = 1 + j_w
    		    sobel_x[ii][jj] = gs_imagem[ii][jj] * xVals[i_f][j_f]
    		    sobel_y[ii][jj] = gs_imagem[ii][jj] * yVals[i_f][j_f]
    		    sobel_whole[ii][jj] = (sobel_x[ii][jj]**2 + sobel_y[ii][jj]**2)**0.5 
    		        
        
cv2.imshow('Sobel X Filter', sobel_x)
cv2.imshow('Sobel Y Filter', sobel_y)
cv2.imshow('Sobel Normalized Filter', sobel_whole)
cv2.waitKey(0)

     
