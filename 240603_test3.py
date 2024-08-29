# 상대적 R값 변경 트랙바
import cv2
import numpy as np

def onChangeRed(pos):
    global img, original_img
    # 현재 트랙바의 R 값을 가져옴
    r = cv2.getTrackbarPos('R', 'Lena color')
    # 선형 보간법을 사용하여 R 값을 조정
    adjustment = int((r / 255.0) * np.max(original_img[:, :, 2]))
    img[:, :, 2] = np.clip(original_img[:, :, 2] * (adjustment / np.max(original_img[:, :, 2])), 0, 255)
    # 변경된 이미지를 다시 디스플레이
    cv2.imshow('Lena color', img)

imageFile = './data/lena.jpg'
img = cv2.imread(imageFile)
original_img = img.copy()


cv2.imshow('Lena color', img)

# 트랙바 생성
cv2.createTrackbar('R', 'Lena color', 0, 255, onChangeRed)

# 초기 R 값을 현재 이미지의 R 채널 평균값으로 설정
initial_r = int(np.mean(original_img[:, :, 2]))
cv2.setTrackbarPos('R', 'Lena color', initial_r)

cv2.waitKey(0)
cv2.destroyAllWindows()
