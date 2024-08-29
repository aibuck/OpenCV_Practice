# 0213.py
import cv2
import matplotlib.pyplot as plt
import matplotlib.animation as animation
 
 # 사용자 정의 클래스
 # 그래프 화면 상에 애니메이션 처리하는 기능을 담당하는 클래스
class Video:
    # 생성자 함수
    def __init__(self, device=0):
        self.cap = cv2.VideoCapture(device)
        # 첫 프레임 얻어서 인스턴스 내부에 저장
        self.retval, self.frame = self.cap.read()
        self.im = plt.imshow(cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB))
        print('start capture ...')
       
    # 생성자에서 얻은 첫 프레임에서 업데이트   
    def updateFrame(self, k):
        self.retval, self.frame = self.cap.read()
        self.im.set_array(cv2.cvtColor(camera.frame, cv2.COLOR_BGR2RGB))
#       return self.im,

    def close(self):
        if self.cap.isOpened():
            self.cap.release()
        print('finish capture.')

# 프로그램 시작 
fig = plt.figure()
fig.canvas.manager.set_window_title('Video Capture')
plt.axis("off")

camera = Video() # 프레임 얻어서 표시하는 역할
##camera = Video('./data/vtest.avi')
ani = animation.FuncAnimation(fig, camera.updateFrame, interval=50)
plt.show()
camera.close()
