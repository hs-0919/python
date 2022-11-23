# XGBoost로 분류 모델 작성
# breast_cancer dataset 사용
# pip install xgboost
# pip install lightgbm = xgboost 보다 성능이 우수하다. 대용량 처리에 효과적
#                        데이터가 적으면 과적합 발생우려가 매우 높다.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xgboost as xgb
from sklearn.datasets import load_breast_cancer
from lightgbm import LGBMClassifier # xgboost 보다 성능이 우수하다. 대용량 처리에 효과적
from sklearn.metrics import r2_score
from xgboost import plot_importance
from sklearn.model_selection import train_test_split
from sklearn import metrics 


dataset = load_breast_cancer()
x_feature = dataset.data
y_label = dataset.target

cancer_df = pd.DataFrame(data=x_feature, columns=dataset.feature_names)
print(cancer_df.head(4), cancer_df.shape) # (569, 30)
print(dataset.target_names) # ['malignant'-양성 'benign'-음성]
# 0이면 malignant 1이면 benign
print(np.sum(y_label == 0)) # 'malignant'-양성 = 212
print(np.sum(y_label == 1)) # 'benign'-음성 = 357

x_train, x_test, y_train, y_test =train_test_split(x_feature, y_label, test_size=0.2, random_state=12)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape) # (455, 30) (114, 30) (455,) (114,)

# model 
model = xgb.XGBClassifier(booster='gbtree', max_depth=6, n_estimators=500).fit(x_train, y_train) # gbtree -의사결정
# model =LGBMClassifier().fit(x_train, y_train)


# print(model)
pred = model.predict(x_test)
print('예측값 : ', pred[:10])
print('실제값 : ', y_test[:10])

acc = metrics.accuracy_score(y_test, pred)
print('acc : ', acc)

print()
cl_rep =metrics.classification_report(y_test, pred)
print('classification_report : \n', cl_rep)

# 중요 변수 시각화 
fig, ax = plt.subplots(figsize=(10,12))
plot_importance(model, ax=ax)
plt.show()

