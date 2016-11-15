import cv2
import numpy as np

img = cv2.imread("index.jpg")


gs_imagem = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

row,col = gs_imagem.shape

for i in range(0,row):
    for j in range(0,col):
	if gs_imagem[i][j]<102:
		gs_imagem[i][j] = 0;
		

cv2.imwrite("Piecewise.png" , gs_imagem)
img1 = cv2.imread("Piecewise.png")
cv2.imshow("Piecewise",img1)
cv2.waitKey(0)        
