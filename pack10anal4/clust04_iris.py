# iris dataset으로 지도학습(KNN) / 비지도학습(K-Means)

from sklearn.datasets import load_iris


iris_dataset = load_iris()
print(iris_dataset['data'][:3])
print(iris_dataset['feature_names'])

# train / test split
from sklearn.model_selection import train_test_split
train_x, test_x, train_y, test_y = train_test_split(iris_dataset['data'], iris_dataset['target'],
                                                    test_size=0.25, random_state=42)
print()
# 지도학습(KNM)
from sklearn.neighbors import KNeighborsClassifier

knnModle= KNeighborsClassifier(n_neighbors=5)
knnModle.fit(train_x, train_y) # feature, label

predict_label = knnModle.predict(test_x)
print(predict_label)

from sklearn import metrics
print('acc : ', metrics.accuracy_score(test_y, predict_label))

print('------------'*30)
# 비지도학습(K-Means)
from sklearn.cluster import KMeans
kmeansModel = KMeans(n_clusters=3, init='k-means++', random_state=0)
kmeansModel.fit(train_x)  # feature 만 줌

print(kmeansModel.labels_)

print('0 cluster :', train_y[kmeansModel.labels_ == 0])
print('1 cluster :', train_y[kmeansModel.labels_ == 1])
print('2 cluster :', train_y[kmeansModel.labels_ == 2])

pred_cluster = kmeansModel.predict(test_x)
print('pred_cluster : ', pred_cluster)

import numpy as np
np_arr = np.array(pred_cluster)
# np_arr[np_arr == 3] = 1
# np_arr[np_arr == 3] = 0
# np_arr[np_arr == 3] = 2

pred_label = np_arr.tolist()  # array에서 -> list로 변형 
print(pred_label)
print('test acc : {:.2f}'.format(np.mean(pred_label == test_y)))

