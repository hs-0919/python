# 밀도 기반 클러스터링: 데이터가 비선형인 경우 일반적인 계층적, 비계층적 클러스터링이 불가.
# 이를 해결하기 위한 방안이 밀도 기반 클러스터링

import matplotlib.pylab as plt
from matplotlib import style
import numpy as np
from sklearn.datasets import make_moons
from sklearn.cluster import KMeans, DBSCAN

# 샘플데이터 
x, y = make_moons(n_samples=200, noise=0.05, random_state=0) # y는 의미없다- 클러스터할꺼라서
print(x)
print('실제 군집 id: ', set(y)) # 실제 군집 id:  {0, 1}
# plt.scatter(x[:, 0], x[:, 1],c='r')
# plt.show()

# KMeans로 군집 분류
km = KMeans(n_clusters=2, random_state=0)
pred1 = km.fit_predict(x)
print('예측 군집 id: ', pred1[:10]) # 10개만 보자
print('예측 군집 id: ', set(pred1))

# KMeans 군집 결과 시각화
def plotFunc(x, pr):
    plt.scatter(x[pr==0, 0], x[pr==0, 1], s=40, c='green', marker='o', label='cluster1')
    plt.scatter(x[pr==1, 0], x[pr==1, 1], s=40, c='red', marker='s', label='cluster2')
    plt.scatter(km.cluster_centers_[:,0], km.cluster_centers_[:,1], s=60, c='yellow', marker='+', label='centroid')
    plt.legend()
    plt.show()

plotFunc(x, pred1) # 완전한 분리가 안됨

# DBSCAN으로 군집 분류
ds=DBSCAN(eps=0.2, min_samples=5, metric='euclidean') # eps - 두 샘플간 최대거리
pred2 = ds.fit_predict(x)
plotFunc(x, pred2)





