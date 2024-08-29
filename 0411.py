# 0411.py
import cv2
src = cv2.imread('./data/lena.jpg')

dst = cv2.split(src) 
print(type(dst)) # 튜플로 구분

# 튜플 내 첫 번째 요소의 타입 : 배열
print(type(dst[0])) # type(dst[1]), type(dst[2])

cv2.imshow('blue',  dst[0])
cv2.imshow('green', dst[1])
cv2.imshow('red',   dst[2])
cv2.waitKey()    
cv2.destroyAllWindows()
