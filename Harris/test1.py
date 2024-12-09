import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('home.jpg')    # 读图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
out = img.copy()
########## Begin ##########
plt.imshow(gray, cmap="gray")
plt.title("Original image")
plt.show()






########## End ##########
cv2.imwrite('out.png', out)