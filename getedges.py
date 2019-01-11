# straight from the opencv docs
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('test.jpg', 0)
edges = cv2.Canny(img, 100, 200)
np.savetxt("raw_edges.csv", edges, delimiter="\n")

# size of edges array
print(edges.shape)

# get indeces of darker edges
edge_indices = np.nonzero(edges)
np.savetxt("edge_indices.csv", edge_indices, delimiter=",")

# get values of indices
rows, cols = np.nonzero(edges)
np.savetxt("edge_values.csv", edges[rows, cols], delimiter="\n")

'''
# REGION OF INTEREST
roi = cv2.selectROI(img)
crop = img[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
cv2.imshow("Image", crop)
cv2.waitKey(0)
'''

# PRINTING OUTPUT
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()
