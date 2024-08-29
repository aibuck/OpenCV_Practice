# 0214.py
import cv2
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 맷플롯립 애니메이션 담당하는 클래스를 상속받아 만든 클래스
class Video(animation.FuncAnimation):
    def __init__(self, device=0, fig=None, frames=None,
                       interval=50, repeat_delay=5, blit=False, **kwargs):

        if fig is None:
            self.fig = plt.figure()
            self.fig.canvas.manager.set_window_title('Video Capture')
            plt.axis("off")

        # 상속해준 부모클래스    
        super(Video, self).__init__(self.fig, self.updateFrame, init_func=self.init,
                                    frames=frames, interval=interval, blit=blit,
                                    repeat_delay=repeat_delay, **kwargs)        
        self.cap = cv2.VideoCapture(device)
        print("start capture ...")

    # 첫 프레임 얻어서 초기화
    def init(self): 
        retval, self.frame = self.cap.read()
        if retval:
            self.im = plt.imshow(cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB))
    
    # 첫 프레임 이후 새 프레임 업데이트
    def updateFrame(self, k):
        retval, self.frame = self.cap.read()
        if retval:
            self.im.set_array(cv2.cvtColor(camera.frame, cv2.COLOR_BGR2RGB))
#       return self.im,
       
    def close(self):
        if self.cap.isOpened():
            self.cap.release()
        print("finish capture.")

# 프로그램 시작 
camera = Video()
##camera = Video('./data/vtest.avi')
plt.show()
camera.close()
