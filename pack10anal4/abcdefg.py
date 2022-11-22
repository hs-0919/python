from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd

data = pd.read_csv('../testdata/titanic_data.csv', usecols=['Survived', 'Pclass', 'Sex', 'Age','Fare'])
print(data.head(2), data.shape) # (891, 12)
data.loc[data["Sex"] == "male","Sex"] = 0
data.loc[data["Sex"] == "female", "Sex"] = 1
print(data["Sex"].head(2))
print(data.columns)

feature = data[["Pclass", "Sex", "Fare"]]
label = data["Survived"] 

# train / test split (7:3)
x_train, x_test, y_train, y_test =train_test_split(feature,label,test_size=0.3, random_state=12)
print(x_train.shape, x_test.shape,y_train.shape, y_test.shape) # (623, 3) (268, 3) (623,) (268,)

# 모델
model = DecisionTreeClassifier(criterion='entropy', random_state=12)
print(model)
model.fit(x_train, y_train)

# 뷴류 예측
y_pred = model.predict(x_test)
print('예측값 : ', y_pred)
print('실제값 : ', y_test)
print('총갯수:%d, 오류수:%d'%(len(y_test), (y_test != y_pred).sum())) # 총갯수:268, 오류수:59

# 분류정확도(accuracy) - 1
print('%.5f'%accuracy_score(y_test, y_pred)) #  0.77985

# 분류정확도(accuracy) - 2
print('test : ', model.score(x_test, y_test))    # 0.77985
print('train : ', model.score(x_train, y_train)) # 0.92455

# 분류정확도(accuracy) - 3
con_mat = pd.crosstab(y_test, y_pred, rownames=['예측치'], colnames=['관측치'])
print(con_mat)
print((con_mat[0][0] + con_mat[1][1]) / len(y_test))  # 0.77985