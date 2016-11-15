import cv2
import numpy as np

def power(imagem, name):
    
    imagem = 2*imagem**1.2
    cv2.imwrite(name, imagem)

img = cv2.imread("index.jpg")


gs_imagem = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gs_imagem = np.float64(gs_imagem)
power(gs_imagem, "PowerLaw.png")
img1 = cv2.imread("PowerLaw.png")
cv2.imshow("PowerLaw",img1)
cv2.waitKey(0)

