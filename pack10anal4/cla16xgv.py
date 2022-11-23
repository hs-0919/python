# 산탄데르 은행 고객만족 여부 분류 모델
# label name: TARGET - 0 이면 만족, 1이면 불만족
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

df = pd.read_csv('train_san.csv', encoding='latin-1')
print(df.head(3), df.shape) # (76020, 371)
print(df.info())

print()
print(df['TARGET'].value_counts()) # 0 - 73012, 1 - 3008
unsatified_cnt = df[df['TARGET'] == 1].TARGET.count()
total_cnt = df.TARGET.count()
print('불만족 비율은 {0:.2f}'.format((unsatified_cnt / total_cnt))) # 불만족 비율은 0.04 4%

# print(df.describe())
# var3변수에 이상치 의심
df['var3'].replace(-999999, 2, inplace=True)
# print(df.describe())
df.drop('ID', axis=1, inplace=True)

x_features =df.iloc[:, :-1]
y_labels = df.iloc[:, -1]
print(x_features.shape, y_labels.shape)  # (76020, 369) (76020,)

# train / test split
x_train, x_test, y_train, y_test =train_test_split(x_features, y_labels, test_size=0.2, random_state=12)
print(x_train.shape, x_test.shape,y_train.shape, y_test.shape) # (60816, 369) (15204, 369) (60816,) (15204,)

train_cnt = y_train.count()
test_cnt = y_test.count()
print('train데이터 레이블 분포 비율 : ', y_train.value_counts() / train_cnt)
print('test데이터 레이블 분포 비율 : ', y_test.value_counts() / test_cnt)

# model 
from  xgboost import XGBClassifier
from sklearn.metrics import roc_auc_score

xgb_clf = XGBClassifier(n_estimators=5, random_state=12)
xgb_clf.fit(x_train, y_train, eval_metric='auc', early_stopping_rounds=2,
            eval_set=[(x_train, y_train), (x_test, y_test)]) # early_stopping_rounds-조기중단파라미터

xgb_roc_curve = roc_auc_score(y_test, xgb_clf.predict_proba(x_test)[:, 1])
print('ROC AUC : {0:.4f}'.format(xgb_roc_curve))
pred = xgb_clf.predict(x_test)
print('예측값 : ', pred[:5])
print('실제값 : ', y_test[:5].values)

from sklearn import metrics
acc = metrics.accuracy_score(y_test, pred)
print('acc : ', acc) # 0.9611



# GridSearchCV로 best parameter 구한 후 모델 작성
# 중요 변수를 알아내 feature를 줄이는 작업
# 성격이 유사한 변수들에 대해 차원 축소를하여 features를 줄이는 작업
# ...








