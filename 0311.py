#0311.py
import numpy as np
import cv2

"""
event : 이벤트에 대한 정보가 담긴 객체
x, y : 이벤트 발생 좌표
flags : 이벤트 처리시 필요한 플래그(힌트)
param : 주어진 부가정보(여기서는 [img])

"""
def onMouse(event, x, y, flags, param):
##    global img
    if event == cv2.EVENT_LBUTTONDOWN:
        if flags & cv2.EVENT_FLAG_SHIFTKEY:
            cv2.rectangle(param[0], (x-5, y-5), (x+5, y+5), (255, 0, 0))
        else:
            cv2.circle(param[0], (x, y), 5, (255, 0, 0), 3)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(param[0], (x, y), 5, (0, 0, 255), 3)        
    elif event == cv2.EVENT_LBUTTONDBLCLK:
        param[0] = np.zeros(param[0].shape, np.uint8) + 255   
    cv2.imshow("img", param[0])
    
img = np.zeros((512,512,3), np.uint8) + 255
cv2.imshow('img', img)

# img 라는 이름의 윈도우에 대해 마우스 이벤트 핸들러로
# onMouse 함수를 등록, 부가 정보는 img가 유일함.
cv2.setMouseCallback('img', onMouse, [img])
cv2.waitKey()
cv2.destroyAllWindows()
