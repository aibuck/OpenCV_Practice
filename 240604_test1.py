#모자이크
import cv2
import numpy as np

src = cv2.imread('./data/boat.jpg')
# src = cv2.resize(src,(800, 800))
dst = np.zeros(src.shape, dtype=src.dtype) + 255

N = 128
# height, width = src.shape
height, width, channel = src.shape # 변수명 _ : 사용 안할 값이라는 의미

h = height // N
w = width // N

for i in range(N):
    for j in range(N):
        y = i*h
        x = j*w       
        roi = src[y:y+h, x:x+w]
        # dst[y:y+h, x:x+w] = cv2.mean(roi)[0]
        dst[y:y+h, x:x+w] = cv2.mean(roi)[0:3]

cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
