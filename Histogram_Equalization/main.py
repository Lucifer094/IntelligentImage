import cv2
import numpy as np


img = cv2.imread('jetplane.png')  # Read image data.
############### Begin #################
(Width, High, Chanel) = img.shape
MaxGray = 255  # 2^8-1
GrayCountOrg = np.zeros((Chanel, MaxGray))  # Save original image gray count.
for ChanelPos in range(0, Chanel):
    for RowPos in range(0, Width):
        for ColPos in range(0, High):
            GrayCountOrg[ChanelPos, img[RowPos, ColPos, ChanelPos]] = \
                GrayCountOrg[ChanelPos, img[RowPos, ColPos, ChanelPos]] + 1

for ChanelPos in range(0, Chanel):  # Sum gray count.
    for GrayPos in range(1, MaxGray):
        GrayCountOrg[ChanelPos, GrayPos] = GrayCountOrg[ChanelPos, GrayPos] + GrayCountOrg[ChanelPos, GrayPos-1]

GrayTrans = np.zeros((Chanel, MaxGray))  # Save each original gray`s transfer gray.
PixSum = Width*High
for ChanelPos in range(0, Chanel):
    for GrayPos in range(0, MaxGray):
        GrayTrans[ChanelPos, GrayPos] = round(MaxGray*(GrayCountOrg[ChanelPos, GrayPos]/PixSum))

########## End ##########
out = img
for ChanelPos in range(0, Chanel):
    for RowPos in range(0, Width):
        for ColPos in range(0, High):
            out[RowPos, ColPos, ChanelPos] = GrayTrans[ChanelPos, out[RowPos, ColPos, ChanelPos]]
cv2.imwrite('out.png', out)
