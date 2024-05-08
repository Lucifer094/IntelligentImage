import matplotlib.pyplot as plt
import cv2
import numpy as np
import math

img = cv2.imread('Lena.png')  # Read image data.
# plt.imshow(img, cmap="gray")
# plt.title("Original image")
# plt.show()
########## Begin ##########

# 1.Using Gaussian function to smooth image.
# 1.1.Create a two-dimensional Gaussian distribution matrix.
sigma1 = sigma2 = 1
gau_sum = 0
gua_win = 5
gua_half_win = 2
gaussian = np.zeros([gua_win, gua_win])
for i in range(gua_win):
    for j in range(gua_win):
        gaussian[i, j] = math.exp(-1/2 * (np.square(i-gua_half_win)/np.square(sigma1) + (np.square(j-gua_half_win)/np.square(sigma2)))) / \
                         (2*math.pi*sigma1*sigma2)
gau_sum = np.sum(gaussian)
gaussian = gaussian/gau_sum
# 1.2.Product image and Gaussian matrix.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
W, H = gray.shape
new_gray = np.zeros([W, H])
for i in range(gua_half_win, W-gua_half_win):
    for j in range(gua_half_win, H-gua_half_win):
        new_gray[i, j] = np.sum(gray[i-gua_half_win:i+gua_half_win+1, j-gua_half_win:j+gua_half_win+1]*gaussian)
# plt.imshow(new_gray, cmap="gray")
# plt.title("Gaussian smooth")
# plt.show()

# 2.Pixel gradient calculation.
IX = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
IY = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
GX = np.zeros([W, H])
GY = np.zeros([W, H])
GXY = np.zeros([W, H])
for i in range(gua_half_win, W-gua_half_win):
    for j in range(gua_half_win, H-gua_half_win):
        GX[i, j] = np.sum(new_gray[i-1:i+2, j-1:j+2]*IX)
        GY[i, j] = np.sum(new_gray[i-1:i+2, j-1:j+2]*IY)
        GXY[i, j] = math.sqrt(pow(GX[i, j], 2) + pow(GY[i, j], 2))
# plt.imshow(GX, cmap="gray")
# plt.title("GX")
# plt.show()
# plt.imshow(GY, cmap="gray")
# plt.title("GY")
# plt.show()
# plt.imshow(GXY, cmap="gray")
# plt.title("GXY")
# plt.show()

# 3.Non-maximum suppression.
NMS = np.copy(GXY)
for i in range(gua_half_win, W-gua_half_win):
    for j in range(gua_half_win, H-gua_half_win):
        if GXY[i, j] == 0:
            NMS[i, j] = 0
        else:
            gradX = GX[i, j]
            gradY = GY[i, j]
            gradTemp = GXY[i, j]
            if np.abs(gradY) > np.abs(gradX):
                weight = np.abs(gradX) / np.abs(gradY)
                grad2 = GXY[i - 1, j]
                grad4 = GXY[i + 1, j]
                if gradX * gradY > 0:
                    grad1 = GXY[i - 1, j - 1]
                    grad3 = GXY[i + 1, j + 1]
                else:
                    grad1 = GXY[i - 1, j + 1]
                    grad3 = GXY[i + 1, j - 1]
            else:
                weight = np.abs(gradY) / np.abs(gradX)
                grad2 = GXY[i, j - 1]
                grad4 = GXY[i, j + 1]
                if gradX * gradY > 0:
                    grad1 = GXY[i + 1, j - 1]
                    grad3 = GXY[i - 1, j + 1]
                else:
                    grad1 = GXY[i - 1, j - 1]
                    grad3 = GXY[i + 1, j + 1]
            gradTemp1 = weight * grad1 + (1 - weight) * grad2
            gradTemp2 = weight * grad3 + (1 - weight) * grad4
            if gradTemp >= gradTemp1 and gradTemp >= gradTemp2:
                NMS[i, j] = gradTemp
            else:
                NMS[i, j] = 0
# plt.imshow(NMS, cmap="gray")
# plt.title("NMS")
# plt.show()

# 4. Hysteresis threshold processing.
TL = 0.05 * np.max(NMS)
TH = 0.7 * np.max(NMS)
DTT = 0 * NMS
for i in range(gua_half_win, W-gua_half_win):
    for j in range(gua_half_win, H-gua_half_win):
        if DTT[i, j] == 1:
            continue
        else:
            if (NMS[i, j] < TL):
                DTT[i, j] = 0
            elif (NMS[i, j] > TH):
                DTT[i, j] = 1
            # else:
            #     DTT[i, j] = 1
            elif ((NMS[i-1, j-1:j+1] < TH).any() or (NMS[i+1, j-1:j+1]).any()
                  or (NMS[i, [j-1, j+1]] < TH).any()):
                DTT[i, j] = 1
plt.imshow(DTT, cmap="gray")
plt.title("DTT")
plt.show()


# # 5. Isolated weak edge suppression.
# DT = 0 * NMS
#
#
# def search_zero(r, c, d):
#     if r <= gua_half_win*4 or r >= W-gua_half_win*4 or \
#             c <= gua_half_win*4 or c >= H-gua_half_win*4:
#         return 1
#     elif np.sum(DTT[r-1:r+2, c-1:c+2]) <= 2:
#         return 1
#     elif np.sum(DT[r-1:r+2, c-1:c+2]) >= 9:
#         return 1
#     elif d < 1:
#         return 1
#     else:
#         for m in range(-1, 2):
#             for n in range(-1, 2):
#                 if DTT[r+m, c+n] > 0:
#                     DT[r+m, c+n] = 1
#                     DTT[r+m, c+n] = 2
#                     search_zero(r+m, c+n, d-1)
#                 else:
#                     continue
#         return 0
#
#
# # for p in range(1, 10):
# for i in range(gua_half_win*2, W-gua_half_win*2):
#     for j in range(gua_half_win*2, H-gua_half_win*2):
#         if DTT[i, j] == 2:
#             DT[i, j] = 1
#             search_zero(i, j, 3)
#         elif DTT[i, j] == 1:
#             for m in range(-1, 2):
#                 for n in range(-1, 2):
#                     if DTT[i+m, j+n] == 2:
#                         DT[i, j] = 1
#                         DTT[i, j] = 2
#                         search_zero(i, j, 3)
#                         break
#                     else:
#                         continue
#         else:
#             continue
#
# plt.imshow(DT, cmap="gray")
# plt.title("DT")
# plt.show()

out = np.copy(DTT)
out = out * 255
out[1:gua_win, 1:H] = 0
out[W-gua_win:W, 1:H] = 0
out[1:W, 1:gua_win] = 0
out[1:W, H-gua_win:H] = 0
########## End ##########
cv2.imwrite('out.png', out)