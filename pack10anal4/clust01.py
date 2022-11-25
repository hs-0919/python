# Clustering(군집화) : 사전정보(label)가 없는 자료에 대해 컴퓨터가 스스로 패턴을 찾아 여러개의 군집을 형성함
# 비지도 학습(군집 분석(Clustering), 주성분 분석(PCA) 등) 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')

np.random.seed(123)
var = ['x','y']
labels = ['점0', '점1', '점2', '점3', '점4']
x = np.random.random_sample([5, 2]) * 10
# print(x)
df = pd.DataFrame(x, columns=var, index=labels)
print(df)

# plt.scatter(x[:, 0], x[:, 1], s=50, c='blue', marker='o')
# plt.grid(True)
# plt.show()

from scipy.spatial.distance import pdist, squareform  # squareform - 표모양

dist_vec = pdist(df, metric='euclidean')  # 데이터(배열)에 대해 각 요소간 거리를 계산한 후 1차원 배열로 반환
print('dist_vec : \n', dist_vec)

row_dist =pd.DataFrame(squareform(dist_vec), columns=labels, index=labels)
print(row_dist)

# 계층적 군집분석 
from scipy.cluster.hierarchy import linkage
row_clusters = linkage(dist_vec, method='complete') # 거리를 넣기 

df = pd.DataFrame(row_clusters, columns=['군집id1', '군집id2', '거리', '멤버수'])
print(df)

# dendrogram으로 row_cluster를 시각화
from scipy.cluster.hierarchy import dendrogram
low_dend = dendrogram(row_clusters, labels=labels)
plt.ylabel('유클리드 거리')
plt.show()

