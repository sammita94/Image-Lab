import cv2
import numpy as np
from matplotlib import pyplot as plt


res = cv2.imread('Edge Detection3.PNG');

gray=cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)

#edges = np.array([0,0,1,1,2,2,3,3,4,4]).reshape(5,2)
edges = cv2.Canny(gray,100,200,apertureSize = 3)

print edges
#Lignes
lines = cv2.HoughLines(edges,1,np.pi/70,110)
for rho,theta in lines[0]:
    if (np.pi/70 <= theta <= np.pi/7) or (2.056 < theta < 4.970) or (1.570 <= theta <= 1.600): #(2,6 <=theta <= 26) or (theta >118 and theta <= 285)

        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho


        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))

        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))

        cv2.line(res,(x1,y1),(x2,y2),(0,0,255),1)

plt.subplot(121),plt.imshow(res, cmap = 'gray')
plt.title('Output'), plt.xticks([]), plt.yticks([])

plt.show()
