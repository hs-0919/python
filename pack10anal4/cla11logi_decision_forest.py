# titanic dataset으로 LogisticRegression, DecisionTree, RandomForest 분류모델 비교

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree._classes import DecisionTreeClassifier

df = pd.read_csv("../testdata/titanic_data.csv")
df.drop(columns=['PassengerId', 'Name', 'Ticket'], inplace=True)
print(df.describe())
print(df.info())
print(df.isnull().sum()) # Age 177, Cabin 687, Embarked 2

# Null 처리 : 평균, 0, 'N' 등으로 변경
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Cabin'].fillna('N', inplace=True)
df['Embarked'].fillna('N', inplace=True)
print(df.head(2))
# print(df.isnull().sum())

# Dtype : object - Sex, Cabin, Embarked 값 들의 상태를 분류해서 보기
print('Sex: ', df['Sex'].value_counts())            # male 577, female 314
print('Cabin: ', df['Cabin'].value_counts())        # Cabin 값들이 너무 복잡하므로 간략하게 정리 - 앞글자만 사용
print('Embarked: ', df['Embarked'].value_counts())

# Cabin 값들이 너무 복잡하므로 간략하게 정리 - 앞글자만 사용
df['Cabin'] = df['Cabin'].str[:1]
print(df.head(5))

print()
# 성별이 생존확률에 어떤 영향을 주었나???????? 궁금해~ 
print(df.groupby(['Sex', 'Survived'])['Survived'].count())
print(233 / (81 + 233)) # 여성은 : 74.2% 생존확률
print(109 / (468 + 109))# 남성은 : 18.9%

# 성별 생존 확률에 대한 시각화
sns.barplot(x='Sex', y='Survived', data=df, ci=95)
plt.show()

# 나이별, Plcass가 생존확률애 어떤 영향을 주었나? ...

print()
# 문자열(object) 데이터를 숫자형으로 변환(범주형)하기
from sklearn import preprocessing # preprocessing - 전처리
# print(set(df['Cabin']))

def labelFunc(datas):
    cols=['Cabin', 'Sex', 'Embarked']
    for c in cols:
        lab=preprocessing.LabelEncoder()
        lab=lab.fit(datas[c])
        datas[c] = lab.transform(datas[c])
    return datas
df = labelFunc(df)
print(df.head(5))
print(df['Cabin'].unique())      # [7 2 4 6 3 0 1 5 8]
print(df['Sex'].unique())        # [1 0]
print(df['Embarked'].unique())   # [3 0 2 1]

print()
feature_df =df.drop(['Survived'], axis='columns')
print(feature_df.head(3))
label_df = df['Survived']
print(label_df.head(3))

x_train, x_test, y_train, y_test =train_test_split(feature_df, label_df, test_size=0.2, random_state=1)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape) # (712, 8) (179, 8) (712,) (179,)

print('---'*30)
# LogisticRegression, DecisionTree, RandomForest 분류모델 비교
logmodel = LogisticRegression(solver='lbfgs', max_iter=500).fit(x_train, y_train) # solber- 약자, max_iter-반복횟수
decmodel = DecisionTreeClassifier().fit(x_train, y_train)
rfmodel = RandomForestClassifier().fit(x_train, y_train)

logpredict = logmodel.predict(x_test)
print('LogisticRegression acc : {0:.5f}'.format(accuracy_score(y_test, logpredict)))
decpredict = decmodel.predict(x_test)
print('DecisionTreeClassifier acc : {0:.5f}'.format(accuracy_score(y_test, decpredict)))
rfpredict = rfmodel.predict(x_test)
print('RandomForestClassifier acc : {0:.5f}'.format(accuracy_score(y_test, rfpredict)))


