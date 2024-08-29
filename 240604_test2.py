# jpg 위에 png 얹기
import cv2
import numpy as np

# 이미지 읽기
src1 = cv2.imread('./data/winter.jpg')
src2 = cv2.imread('./data/cat.png')

# 고양이 이미지 리사이즈
src2 = cv2.resize(src2, (320, 240))
cv2.imshow('src2', src2)

# 고양이 이미지 크기 가져오기
rows, cols, _ = src2.shape

# 윈터 이미지에 고양이 이미지 얹기
# 시작 위치 설정 (예: 윈터 이미지의 왼쪽 상단에 고양이 이미지 위치)
y_offset = 400
x_offset = 100

# ROI 설정
roi = src1[y_offset:y_offset + rows, x_offset:x_offset + cols]

# 고양이 이미지 마스크 생성 및 반전 마스크 생성
src2_gray = cv2.cvtColor(src2, cv2.COLOR_BGR2GRAY)
_, mask = cv2.threshold(src2_gray, 1, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# 배경에서 ROI의 해당 부분을 복사
src1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

# 고양이 이미지에서 고양이 부분만 복사
src2_fg = cv2.bitwise_and(src2, src2, mask=mask)

# 배경과 고양이 이미지를 합성
dst = cv2.add(src1_bg, src2_fg)

# 합성된 이미지를 원본 윈터 이미지에 삽입
src1[y_offset:y_offset + rows, x_offset:x_offset + cols] = dst

# 결과 출력
cv2.imshow('result', src1)
cv2.waitKey(0)
cv2.destroyAllWindows()
