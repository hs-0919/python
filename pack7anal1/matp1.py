# Matplotlib
# - http:// matplotlib.org
# - 플로팅 라이브러리로 matplotlib.pyplot 모듈을 사용하여 그래프 등의 시각화 가능
# - 그래프 종류 : line, scatter, contour 등고선 ), surface, bar , histogram, box,
# - Figure
# 모든 그림은 Figure 라 부르는 matplotlib figure Figure 클래스 객체에 포함
# 내부 plot 이 아닌 경우에는 Figure 는 하나의 아이디 숫자와 window 를 갖는다
# figure()를 명시적으로 적으면 여러 개의 윈도우를 동시에 띄우게 된다
# 상관계수 - 두변수간의 관계성을 보여줌 관계의 방향을 알 수 있다

import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic') # 한글깨짐 방지
plt.rcParams['axes.unicode_minus'] = False  # 음수 깨짐 방지 - 위 랑 세트로 다니면 좋다.

# x = ['서울','수원','인천',] # set은 안됨 / 튜플 가능
# y = [5,3,7]
# plt.xlim([-2, 3])
# plt.ylim([0, 10])
# plt.plot(x,y)
# plt.yticks(list(range(-3, 11, 3)))  # 음수 깨짐
# plt.show()

# data = np.arange(1, 11, 2)
# print(data)
# plt.plot(data)
# x = [0,1,2,3,4]
# for a, b in zip(x, data):
#     # print(a,b)
#     plt.text(a, b, str(b))
#     # y축은 밸류값
# plt.show()

# x = np.arange(10)
# y = np.sin(x)
# print(x, y)
# plt.plot(x, y, 'go--', linewidth=2, markersize=10) # '' - style-- bo - 파란색 동그라미, r+ - 빨간색 +, go--
# plt.show()

# hold : 복수의 차트를 하나의 영역에 겹쳐서 출력
# x = np.arange(0, np.pi*3, 0.1)
# y_sin = np.sin(x)
# y_cos = np.cos(x)
#
# plt.scatter(x, y_cos)
# plt.plot(x, y_sin, 'r+')
#
# plt.title('싸인 앤드 코카인')
# plt.legend(['사인','코사인'])
# plt.show()
#
# print()
# # subplot : Figure를 여러 개로 나눔
# plt.subplot(2,1,1)
# plt.plot(x, y_sin, 'y+')
# plt.subplot(2,1,2)
# plt.scatter(x, y_cos)
# plt.show()

irum = 'a','b','c','d','e'
kor = [80, 50, 70, 70, 90]
eng = [60, 70, 80, 70, 60]
plt.plot(irum, kor, 'rs--')
plt.plot(irum, eng, 'gs--') 
plt.ylim([0, 100])
plt.legend(['국어', '영어'], loc=3)  # loc는 시계 반대방향으로 1,2,3,4 이다.
plt.grid(True)

fig = plt.gcf()
plt.show()
fig.savefig('차트.png')

from matplotlib.pyplot import imread
img = imread('차트.png') # 이미지 불러오기
plt.imshow(img)
plt.show()


