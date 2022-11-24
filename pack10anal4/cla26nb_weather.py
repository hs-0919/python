# 날씨 정보로 나이브에즈로 분류기 작성 - 비 예보
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn import metrics


df = pd.read_csv("../testdata/weather.csv")
print(df.head(5))
print(df.info())

features = df[['MinTemp', 'MaxTemp', 'Rainfall']]
# labels = df['RainTomorrow'].apply(lambda x:1 if x =='Yes' else 0)
labels = df['RainTomorrow'].map({'Yes':1, 'No': 0})

print(features[:3])
print(labels[:3])
print(set(labels))  # {0, 1}

# split
x_train, x_test, y_train, y_test =train_test_split(features, labels, test_size=0.25, random_state=1)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape) # (274, 3) (92, 3) (274,) (92,)

# model 
gmodel = GaussianNB()
gmodel.fit(x_train, y_train)

pred = gmodel.predict(x_test)
print('예측값 : ', pred[:10])
print('실제값 : ', y_test[:10].values)

acc =sum(y_test == pred) / len(pred)
print('acc : ', acc)
print('acc : ', accuracy_score(y_test, pred))

# kfold
from sklearn import model_selection
cross_val = model_selection.cross_val_score(gmodel, features, labels, cv=5)
print('교차 검증 : ', cross_val)
print('교차 검증 평균 : ', cross_val.mean())

print('새로운 자료로 분류 예측')
import numpy as np
new_weather = np.array([[8.0, 24.3, 0.0], [10.0, 25.3, 10.0], [10.0, 30.3, 5.0]])
print(gmodel.predict(new_weather))

