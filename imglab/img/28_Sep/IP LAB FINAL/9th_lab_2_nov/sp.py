import cv2
import numpy as np
from matplotlib import pyplot as plt

R = 5
C = 5
 
def minCost(cost, m, n):
 
    # Instead of following line, we can use int tc[m+1][n+1] or
    # dynamically allocate memoery to save space. The following
    # line is used to keep te program simple and make it working
    # on all compilers.
    tc = [[0 for x in range(C)] for x in range(R)]
 
    tc[0][0] = cost[0][0]
    #tc[0][0] = 0

    # Initialize first column of total cost(tc) array
    for i in range(1, m+1):
        tc[i][0] = tc[i-1][0] - cost[i][0]
 	#tc[i][0] = 0

    # Initialize first row of tc array
    for j in range(1, n+1):
        tc[0][j] = tc[0][j-1] - cost[0][j]
 	#tc[0][j] = 0

    # Construct rest of the tc array
    for i in range(1, m+1):
        for j in range(1, n+1):
            tc[i][j] = min(tc[i-1][j-1], tc[i-1][j], tc[i][j-1]) + cost[i][j]
    print "cost matrix"
    print tc
    print "\n"
    print "cost of shortest path = "
    return tc[m][n]
 
# Driver program to test above functions



img = cv2.imread('beach.jpg')


"""height, width, channels = img.shape
print height, width, channels"""

res = cv2.resize(img, (5,5),fx=0, fy=0, interpolation = cv2.INTER_LINEAR)

gray = cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)

data = np.asarray( gray, dtype="int32" )
print "image pixels"
print data
print "\n"


print (minCost(data, 4, 4))


plt.subplot(211),plt.imshow(img)
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(212),plt.imshow(res)
plt.title('Output'), plt.xticks([]), plt.yticks([])
plt.show()
