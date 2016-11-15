import cv2
import numpy as np
from matplotlib import pyplot as plt

def bit_plane(name, b):
    
    gs_imagem = cv2.imread("trial.png" , 0)
    result = np.int64(gs_imagem)
    num = 2**b
    row,col = result.shape
    for i in range(0,row):
        for j in range(0,col):
	    bit = int(result[i][j]) // num
	    if bit % 2 == 0:
	    	result[i][j] = 0
	    else:
	    	result[i][j] = 255
	    

    name = name+ str(b) +".png"
    cv2.imwrite(name, result)
	 
	 
#gs_imagem = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
for i in range(0,8):

    bit_plane("BitPlane",i)
    name = "BitPlane" + str(i) + ".png"
    img1 = cv2.imread(name)
    cv2.imshow(name,img1)
    cv2.waitKey(0)


