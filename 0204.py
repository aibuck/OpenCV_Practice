# 0204.py
import cv2
from   matplotlib import pyplot as plt

imageFile = './data/lena.jpg'
imgGray = cv2.imread(imageFile, cv2.IMREAD_GRAYSCALE)
plt.axis('off')

# interpolation(보간) : 픽셀 사이에 누락된 픽셀이 있을 경우 메운다.
plt.imshow(imgGray, cmap = "gray", interpolation='bicubic')
plt.show()
