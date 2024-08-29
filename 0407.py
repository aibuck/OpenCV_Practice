# 0407.py
import cv2
 
src = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)
roi = cv2.selectROI(src) # 마우스 드래그로 ROI 선택 함수
print('roi =', roi) # (x, y, w, h)

if roi != (0, 0, 0, 0):
    img = src[roi[1]:roi[1]+roi[3], # y, h
               roi[0]:roi[0]+roi[2]] # x, w

    cv2.imshow('ROI', img)
    cv2.waitKey()
    
cv2.destroyAllWindows()
