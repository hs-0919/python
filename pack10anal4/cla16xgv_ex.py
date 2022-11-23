# 'glass datasets' 유리 식별 데이터베이스

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

df = pd.read_csv('../testdata/glass.csv')
print(df.head(5))
print(df.shape) # (214, 10)
print(df.info())

print()
print(df['Type'].value_counts()) 
# type 1 - 70, 2 - 76, 3 - 17, 4 - 0, 5 - 13, 6 - 9, 7 -29
type_cnt = df[df['Type'] == 1].Type.count()
otherType_cnt = df.Type.count()
print('Type1의 비율은 {0:.2f}'.format((type_cnt / otherType_cnt))) # 33%

print()
x_features =df.iloc[:, :-1]
y_labels = df.iloc[:, -1]
print(x_features.shape, y_labels.shape)  # (214, 9) (214,)

# train / test split
x_train, x_test, y_train, y_test =train_test_split(x_features, y_labels, test_size=0.3, random_state=12)
print(x_train.shape, x_test.shape,y_train.shape, y_test.shape) # (171, 9) (43, 9) (171,) (43,)

train_cnt = y_train.count()
test_cnt = y_test.count()
print('train데이터 레이블 분포 비율 : ', y_train.value_counts() / train_cnt)
print('test데이터 레이블 분포 비율 : ', y_test.value_counts() / test_cnt)

# model 
from  xgboost import XGBClassifier
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import LabelEncoder
from sklearn import metrics

le = LabelEncoder()
y_train = le.fit_transform(y_train)
print(y_train[:5], set(y_train)) # [4 1 1 2 5] {0, 1, 2, 3, 4, 5}


xgb_clf = XGBClassifier(n_estimators=5, random_state=12)
xgb_clf.fit(x_train, y_train, eval_metric='auc', early_stopping_rounds=2,
            eval_set=[(x_train, y_train), (x_test, y_test)]) # early_stopping_rounds-조기중단파라미터

xgb_roc_curve = roc_auc_score(y_test, xgb_clf.predict_proba(x_test), multi_class='ovr') # multi_class='ovr' 추가!!
print('ROC AUC : {0:.4f}'.format(xgb_roc_curve))
pred = xgb_clf.predict(x_test)
print('예측값 : ', pred[:5])
print('실제값 : ', y_test[:5].values)
print('정확도 : ', metrics.accuracy_score(y_test, pred)) # 정확도 :  0.0697

from sklearn import metrics
acc = metrics.accuracy_score(y_test, pred)
print('acc : ', acc) # acc :  0.0697

