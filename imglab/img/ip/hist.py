import cv2
import numpy as np
from matplotlib import pyplot as plt
 
img = cv2.imread('img1.jpg',0)
print img
 
hist,bins = np.histogram(img.flatten(),[0,256])

plt.hist(img.flatten(),256,[0,256], color = 'b')


plt.show()
