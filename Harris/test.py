import cv2
import numpy as np
import matplotlib.pyplot as plt



# original image
img = cv2.imread('home.jpg')#读图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
h, w, c = img.shape

# harris dst
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gray = np.float32(gray)
dst = cv2.cornerHarris(gray, blockSize=3, ksize=5, k=0.05)
image_dst = img[:, :, :]
image_dst[dst > 0.01 * dst.max()] = [0, 0, 255]


cv2.imwrite('out.png', image_dst)


