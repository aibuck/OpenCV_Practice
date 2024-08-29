# 0401.py
import cv2
import numpy as np

img = cv2.imread('./data/lena.jpg') # cv2.IMREAD_COLOR
##img = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)

print('img.ndim=', img.ndim) # 몇 차원?
print('img.shape=', img.shape)
print('img.dtype=', img.dtype) # 자료형?

## np.bool, np.uint16, np.uint32, np.float32, np.float64, np.complex64
img=img.astype(np.int32) #강제 형 변환
print('img.dtype=',img.dtype)

img=np.uint8(img)
print('img.dtype=',img.dtype)
