import cv2
import numpy as np

 

gs_imagem = cv2.imread("index.jpg",0)
cv2.imshow("Original",gs_imagem) 

row,col = gs_imagem.shape

for i in range(0,row):
    for j in range(0,col):
        summ = 0
        count = 0
    	for ii in range(i-1,i+2):
    		for jj in range(j-1,j+2):
    		    if ii >= 0 and ii <row and jj >=0 and jj <col :
    		        summ += gs_imagem[ii][jj]
    		        count += 1
        gs_imagem[i][j] = summ/count
        
cv2.imshow("Mean Filter",gs_imagem)
cv2.waitKey(0)      
     
