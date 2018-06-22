import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('sources/full/00a2e771a353865c080119b82bcc5d2258e9bb2b.jpg',0)
edges = cv2.Canny(img,100,200)
 
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()