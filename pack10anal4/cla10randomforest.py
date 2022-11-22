# Random forest는 ensemble(앙상블) machine learning 모델입니다. 
# 여러개의 decision tree를 형성하고 새로운 데이터 포인트를 각 트리에 동시에 통과시키며, 
# 각 트리가 분류한 결과에서 투표를 실시하여 가장 많이 득표한 결과를 최종 분류 결과로 선택합니다. 
# Bagging 방식을 사용
# Titanic dataset

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np


df = pd.read_csv("../testdata/titanic_data.csv")
print(df.head(3))
print(df.columns)
print(df.info())
print(df.isnull().any())

df= df.dropna(subset=['Pclass', 'Age', 'Sex'])  
print(df.shape) # (714, 12)

df_x =df[['Pclass', 'Age', 'Sex']] # feature
print(df_x.head(3))

# scaling
from sklearn.preprocessing import LabelEncoder, OneHotEncoder


# Sex column은 dummy화 - 0 과  1로 바꿈
df_x.loc[:, 'Sex']=LabelEncoder().fit_transform(df_x['Sex']) # 1번 방법
print(df_x.head(5)) # male=1 , female=0
# df_x['Sex'] = df_x['Sex'].apply(lambda x:1 if x == 'male' else 0) # 2번 방법
print(df_x.head(5))
# print(set(df_x['Pclass']))   # {1, 2, 3}

df_y = df['Survived']
print(df_y.head(5))

# Pclass 열에 대한 원핫인코딩(
# 해당 열 범주의 종류만큼 벡터의 크기를 설정하고, 범주에 해당하는 index에 1을 주고 나머지 요소 모두에는 0으로 채우기 )
df_x2 = pd.DataFrame(OneHotEncoder().fit_transform(df_x['Pclass'].values[:, np.newaxis]).toarray(),
                     columns=['f_class', 's_class', 't_class'], index=df_x.index)

print(df_x2.head(2))

df_x = pd.concat([df_x, df_x2], axis=1)
print(df_x.head(3))

# train/test split
x_train, x_test, y_train, y_test =train_test_split(df_x, df_y, test_size=0.25, random_state = 12)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)  # (535, 6) (179, 6) (535,) (179,)

# model
model = RandomForestClassifier(n_estimators=500, criterion='entropy')
model.fit(x_train, y_train)

pred = model.predict(x_test)
print(' 예측값 : ', pred[:5]) #  예측값 :  [1 0 0 0 0]
print(' 실제값 : ', np.array(y_test[:5])) #  실제값 :  [1 0 0 0 1]

# 정확도
print('acc : ', sum(y_test == pred) / len(y_test)) # acc :  0.8379888268156425
from sklearn.metrics import accuracy_score
print('acc : ', accuracy_score(y_test, pred))  # acc :  0.8044692737430168

# 교차 검증
from sklearn.model_selection import cross_val_score
cross_vali = cross_val_score(model, df_x, df_y, cv=5)
print(cross_vali)
print(np.mean(cross_vali))

# 중요 변수
print('특성(변수) 중요도 : ', model.feature_importances_)

import matplotlib.pyplot as plt

def plot_importance(model):
    n_features = df_x.shape[1]
    plt.barh(range(n_features), model.feature_importances_, align='center')
    plt.yticks(np.arange(n_features), df_x.columns)
    plt.xlabel('feature_importances')
    plt.ylabel('feature')
    plt.show()

plot_importance(model)




