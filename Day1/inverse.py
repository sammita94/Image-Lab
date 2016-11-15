import cv2
import numpy as np

def inverse(imagem, name):
    
    imagem =(255-imagem)
    cv2.imwrite(name, imagem)


img = cv2.imread("index.jpg")
gs_imagem = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gs_imagem = np.float64(gs_imagem)
inverse(gs_imagem, "inverse.png")
img1 = cv2.imread("inverse.png")
cv2.imshow("Inverted image",img1)
cv2.waitKey(0)

