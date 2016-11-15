import cv2
import numpy as np

def log(imagem, name):
    
    imagem=imagem+1
    cv2.log(imagem,imagem)
    cv2.normalize(imagem,imagem,0,255,cv2.NORM_MINMAX)
    cv2.convertScaleAbs(imagem,imagem)
   
    cv2.imwrite(name, imagem)

img = cv2.imread("index.jpg")


gs_imagem = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gs_imagem = np.float64(gs_imagem)
log(gs_imagem, "log.png")
img1 = cv2.imread("log.png")
cv2.imshow("Log",img1)
cv2.waitKey(0)

