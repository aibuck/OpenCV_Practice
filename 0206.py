# 0206.py
import cv2
from   matplotlib import pyplot as plt

path = './data/'
imgBGR1 = cv2.imread(path+'lena.jpg')
imgBGR2 = cv2.imread(path+'apple.jpg')
imgBGR3 = cv2.imread(path+'baboon.jpg')
imgBGR4 = cv2.imread(path+'orange.jpg')

imgRGB1 = cv2.cvtColor(imgBGR1, cv2.COLOR_BGR2RGB)
imgRGB2 = cv2.cvtColor(imgBGR2, cv2.COLOR_BGR2RGB)
imgRGB3 = cv2.cvtColor(imgBGR3, cv2.COLOR_BGR2RGB)
imgRGB4 = cv2.cvtColor(imgBGR4, cv2.COLOR_BGR2RGB)

# shaerey = True : x, y 축을 모든 그래프가 공유한다.
fig, ax = plt.subplots(2, 2, figsize=(10,10), sharey=True)
fig.canvas.manager.set_window_title('Sample Pictures')

"""
'auto': 기본 값으로, 이미지의 원래 종횡비를 유지합니다.
'equal': X와 Y 축의 단위 길이가 동일하게 설정되어, 종횡비가 1:1로 설정됩니다. 즉, 스퀘어 픽셀로 표시됩니다.
임의의 숫자: 특정 종횡비를 강제로 설정할 수도 있습니다. 예를 들어, aspect=0.5로 설정하면 Y축이 X축의 절반 길이로 설정됩니다.
"""
ax[0][0].axis('off')
ax[0][0].imshow(imgRGB1, aspect = 'auto')

ax[0][1].axis('off')
ax[0][1].imshow(imgRGB2, aspect = 'auto')

ax[1][0].axis("off")
ax[1][0].imshow(imgRGB3, aspect = "auto")

ax[1][1].axis("off")
ax[1][1].imshow(imgRGB4, aspect = 'auto')

plt.subplots_adjust(left=0, bottom=0, right=1, top=1,
                    wspace=0.05, hspace=0.05)
"""
'tight': 그림 주위의 여백을 최소화합니다. 플롯의 내용에 최대한 가깝게 그림을 저장합니다.
None(기본 값): 여백을 포함하여 그림을 저장합니다.
Bbox 객체: 특정 Bbox를 제공하여 그 영역만 저장합니다.
"""
plt.savefig("./data/0206.png", bbox_inches='tight')
plt.show()
