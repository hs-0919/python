# 나이브 베이즈는 분류기를 만들 수 있는 간단한 기술로써 단일 알고리즘을 통한 훈련이 아닌 
# 일반적인 원칙에 근거한 여러 알고리즘들을 이용하여 훈련된다. 모든 나이브 베이즈 분류기는 
# 공통적으로 모든 특성 값은 서로 독립임을 가정한다. 

from sklearn.naive_bayes import GaussianNB
import numpy as np
from sklearn import metrics

# 조건부 확률   P(Label|Feature)사후확률 = P(Feature|Label)가능도 * P(Label) / p(Feature)

x = np.array([1,2,3,4,5])
x = x[:, np.newaxis]
print(x)
y= np.array([1,3,5,7,9])

model = GaussianNB().fit(x,y)
print(model)
pred = model.predict(x)
print('분류정확도 : ', metrics.accuracy_score(y, pred)) # 분류정확도 :  1.0 100%

# 새로운 값으로 예측

new_x = np.array([[0.5], [0.1], [5], [15]])
new_pred = model.predict(new_x)
print('새로운 예측 결과 : ', new_pred)














