import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图像
image = cv2.imread('house.png', cv2.IMREAD_GRAYSCALE)
########## Begin ##########
out = image


def compute_gradients(image):
    # 使用OpenCV的Sobel算子计算x和y方向的梯度
    grad_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
    grad_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)

    # 计算梯度的幅值和方向
    magnitude, angle = cv2.cartToPolar(grad_x, grad_y, angleInDegrees=True)

    return magnitude, angle


def phase_grouping_simplified(angle_image, threshold=22.5):
    # 简化版的相位编组：将角度图像量化为几个区间
    quantized_angles = np.floor(angle_image / threshold).astype(np.int) * threshold

    # 这里只是简单地量化了角度，并没有实现真正的编组逻辑
    # 真正的编组可能需要额外的逻辑来连接相同方向的像素

    return quantized_angles


def fit_lines(quantized_angles, image_shape):
    # 这里只是示例，并没有实现实际的直线拟合
    # 在实际应用中，可以使用Hough变换或其他方法拟合直线

    # 假设我们已经有了一些直线（这里只是随机生成）
    lines = []
    for _ in range(5):  # 假设有5条直线
        rho = np.random.randint(-image_shape[1] // 2, image_shape[1] // 2)
        theta = np.random.uniform(-90, 90)
        lines.append((rho, theta))

    return lines


# 计算梯度和方向
magnitude, angle = compute_gradients(image)

# 简化版的相位编组
quantized_angles = phase_grouping_simplified(angle)

# 直线拟合（这里只是示例）
lines = fit_lines(quantized_angles, image.shape)

# 绘制直线（仅用于演示）
for line in lines:
    rho, theta = line
    a = np.cos(np.deg2rad(theta))
    b = np.sin(np.deg2rad(theta))
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))

    cv2.line(out, (x1, y1), (x2, y2), (0, 0, 255), 2)

# 显示图像
plt.imshow(out, cmap='gray')
plt.show()
########## End ##########
cv2.imwrite('out.png', out)