import math

# 定义参数
mu_X = 0  # X的均值
mu_Y = 0  # Y的均值
sigma_X = 1  # X的标准差
sigma_Y = 1  # Y的标准差
rho = 0  # X和Y的相关系数

# 给定的点
x = 0
y = 0

# 计算标准化项
z = ((x - mu_X) / sigma_X) ** 2 - 2 * rho * ((x - mu_X) / sigma_X) * ((y - mu_Y) / sigma_Y) + (
            (y - mu_Y) / sigma_Y) ** 2

# 计算PDF值
# 注意：这里我们使用了1 - rho**2的平方根作为分母的一部分，确保分母不为0（当rho接近1时）
pdf_value = (1 / (2 * math.pi * sigma_X * sigma_Y * math.sqrt(1 - rho ** 2))) * math.exp(-z / (2 * (1 - rho ** 2)))

print(f"The probability density at ({x}, {y}) is {pdf_value:.5f}")

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import multivariate_normal

# 定义均值向量和协方差矩阵
mu = np.array([0.0, 0.0])
cov = np.array([[1.0, 0], [0, 1.0]])  # 这里设定了相关系数为0.5

# 创建一个二维网格
x = np.linspace(-3.0, 3.0, 100)
y = np.linspace(-3.0, 3.0, 100)
X, Y = np.meshgrid(x, y)
pos = np.dstack((X, Y))

# 计算二维正态分布的PDF值
rv = multivariate_normal(mean=mu, cov=cov)
Z = rv.pdf(pos)

# 绘制等高线图
fig1 = plt.figure(figsize=(8, 6))
ax1 = fig1.add_subplot(111)
CS = ax1.contour(X, Y, Z)
ax1.clabel(CS, inline=True, fontsize=8)
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_title('Contour plot of 2D Gaussian distribution')
plt.show()

# 绘制三维曲面图
fig2 = plt.figure(figsize=(8, 6))
ax2 = fig2.add_subplot(111, projection='3d')
ax2.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Probability Density')
ax2.set_title('Surface plot of 2D Gaussian distribution')
plt.show()