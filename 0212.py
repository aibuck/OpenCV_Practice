# 0212.py
import cv2
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 프로그램 시작    
cap = cv2.VideoCapture(0)
fig = plt.figure(figsize=(10, 6)) # fig.set_size_inches(10, 6)
fig.canvas.manager.set_window_title('Video Capture')
plt.axis('off')

# 초기화 , <밑 주석 내용> + 첫 프레임 저장
def init():
    global im # 전역변수를 함수 지역 안에서 사용하겠다는 선언
    retval, frame = cap.read() # 첫 프레임 캡처
    im = plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
##    return im,

# 계속적으로 얻어지는 프레임들로 이미지를 업데이트
def updateFrame(k): 
    retval, frame = cap.read()
    if retval:
        im.set_array(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

# 애니메이션 처리 전용 함수
# 그래프화면, 애니메이션 처리함수, 초기화 함수, 시간추가(ms)
ani = animation.FuncAnimation(fig, updateFrame, init_func=init, interval=50)
plt.show()
if cap.isOpened():
    cap.release()
