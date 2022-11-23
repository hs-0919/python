import pandas as pd
import numpy as np
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

df = pd.read_csv('../testdata/Heart.csv')
print(df.head(5), df.shape) # (303, 15)
print(df.columns)
print(df.info())
print(df.isnull())

df = df.fillna(df.mean())
print(df.head(5), df.shape) # (303, 15)
print(df.isnull())

feature= df[['Age', 'Sex', 'RestBP', 'Chol', 'Fbs',
       'RestECG', 'MaxHR', 'ExAng', 'Oldpeak', 'Slope', 'Ca']]
label = df['AHD']

# train / test split (7:3)
x_train, x_test, y_train, y_test =train_test_split(feature,label,test_size=0.3, random_state=12)
print(x_train.shape, x_test.shape,y_train.shape, y_test.shape) # (212, 11) (91, 11) (212,) (91,)

print()
# model
model = svm.SVC(C=0.1).fit(x_train, y_train) # C=0.01 숫자가 작을수록 과적합 방지

pred = model.predict(x_test)
print('예측값 : ', pred[:10])
print('실제값 : ', y_test[:10].values)

acc = metrics.accuracy_score(y_test, pred)
print('acc : ', acc) # acc :  0.5444

print()
# 교차 검증
from sklearn import model_selection
cross_vali = model_selection.cross_val_score(model, feature, label, cv=3) # cv=3 -> kfold-몇개로 접을꺼니~~
print('각각의 검증 정확도 : ', cross_vali)
print('평균 검증 정확도 : ', cross_vali.mean())


# 새 값으로 예측
new_x=[[63,1,145,233,1,2,150,0,2.3,3,0]]
new_pred=model.predict(new_x)
new_x2=[[67,1,160,286,0,2,108,1,1.5,2,3]]
new_pred2=model.predict(new_x2)
print(new_pred, new_pred2) # ['No'] ['No']

