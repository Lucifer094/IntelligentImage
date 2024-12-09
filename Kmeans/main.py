import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('cherry.png')#读图
plt.subplot(121)
plt.imshow(img)
########## Begin ##########
out = img
row = img.shape[0]
col = img.shape[1]


def knn(data, iter, k):
    data = data.reshape(-1, 3)
    data = np.column_stack((data, np.ones(row * col)))
    # 1.随机产生初始簇心
    cluster_center = data[np.random.choice(row * col, k)]
    # 2.分类
    distance = [[] for i in range(k)]
    for i in range(iter):
        print("迭代次数：", i)
        # 2.1距离计算
        for j in range(k):
            print(cluster_center[j, 0:3])
            distance[j] = np.sqrt(np.sum((data[:, 0:3] - cluster_center[j, 0:3]) ** 2, axis=1))
        # 2.2归类
        data[:, 3] = np.argmin(distance, axis=0)
        # 3.计算新簇心
        for j in range(k):
            if np.any(data[:, 3] == j):
                cluster_center[j] = np.mean(data[data[:, 3] == j], axis=0)
            else:
                cluster_center[j] = np.column_stack((np.random.rand(1, 3) * 255, np.ones(1)))
    return data[:, 3]


k = 5
image_show = knn(img, 100, k)

image_show = image_show.reshape(row, col)
out = image_show*(255/k)
plt.subplot(122)
plt.imshow(image_show, cmap='gray')
plt.show()

########## End ##########
cv2.imwrite('out.png', out)