# Ensemble Learning : 개별적인 여러 모델들을 모아 종합적으로 취합 후 분류 결과를 출력
# 종류로는 voting, bagging, boosting 방법이 있다.
# breast_cancer dataset을 사용
# LogisticRegreession, DecisionTree, KNN을 사용하여 보팅 분류기 작성

import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


cancer = load_breast_cancer()
data_df = pd.DataFrame(cancer.data, columns = cancer.feature_names)
print(data_df.head(2))

# train/test split
x_train, x_test, y_train, y_test =train_test_split(cancer.data, cancer.target, random_state=1, test_size=0.2)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape) # (426, 30) (143, 30) (426,) (143,)
print(x_train[:3])
print(y_train[:3], set(y_train)) # [0 0 1] {0, 1} - 0(양성) 과 1(음성) 밖에 없다

# Ensemble model(VotingClassifier) : LogisticRegression + KNN + DecisionTreeClassifier
logi_regreesion = LogisticRegression()
knn = KNeighborsClassifier(n_neighbors = 3)
demodel = DecisionTreeClassifier()

voting_model = VotingClassifier(estimators=[('LR', logi_regreesion), ('KNN', knn), ('Decision', demodel)],
                                voting='soft') # estimators - 모델 , voting='soft' 와 'hard'가 있다.

classifiers = [logi_regreesion, knn, demodel]

# 개별 모델의 학습 및 평가
for classifier in classifiers:
    classifier.fit(x_train, y_train)
    pred = classifier.predict(x_test)
    class_name = classifier.__class__.__name__
    print('{0} 정확도 : {1:.4f}'.format(class_name, accuracy_score(y_test, pred)))
    # warnig 경고 무시해도 됨
    # LogisticRegression 정확도 : 0.9474
    # KNeighborsClassifier 정확도 : 0.9211
    # DecisionTreeClassifier 정확도 : 0.9474

# 앙상블 모델의 학습 및 평가
voting_model.fit(x_train, y_train)
vpred =voting_model.predict(x_test)
print('앙상블 모델의 정확도 : {0:.4f}'.format(accuracy_score(y_test, vpred))) # 0.9474

# bagging 병렬, boosting 직렬 학습

