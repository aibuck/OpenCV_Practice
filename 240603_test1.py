# RBG 트랙바 생성
import numpy as np
import cv2

width, height = 512, 512
x, y, R = 256, 256, 50

while True:
    key = cv2.waitKeyEx(20) # 키 입력 20ms 기다림

    # ESC 입력받으면 break    
    if key == 0x1B:
        break
    
    # 방향키 방향에 따라 한번만 이동
    elif key == 0x270000: # right
        x += 10
    elif key == 0x280000: # down
        y += 10
    elif key == 0x250000: # left
        x -= 10
    elif key == 0x260000: # up
        y -= 10
    
    # 경계확인
    if x < R:
        x = R
    if x > width - R:
        x = width - R
    if y < R:
        y = R
    if y > height - R:
        y = height - R
        
    # 지우고, 그리기 / 원의 좌표가 바뀐다? => 원이 다른 위치에 그려진다.        
    img = np.zeros((height, width, 3), np.uint8) + 255 # 지우기
    cv2.circle(img, (x, y), R, (0, 0, 255), -1) 
    cv2.imshow('img', img)
    
cv2.destroyAllWindows()
