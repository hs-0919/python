# ROC ()curve
# ROC 커브는 모든 가능한 threshold 에대해 분류모델의 성능을 평가하는데 사용됩니다.
# ROC커브는아래의 영역을 AUC(Area Under thet Curve)라 합니다.

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix



x, y = make_classification(n_samples=100, n_features=2, n_redundant=0, random_state=123)
print(x[:5])
print(y[:5])

# plt.scatter(x[:, 0], x[:, 1])
# plt.show()

model =LogisticRegression().fit(x,y)
y_hat = model.predict(x) # 예측값
print('y_hat : ', y_hat[:5])

print()
f_value = model.decision_function(x) # 판별함수(결정함수) : 판별 경계선 설정을 위한 샘플 자료 얻기
# print('f_value: ', f_value) # 0이하는 0으로 취급, 0초과일때 1로 표시 -참고-

df= pd.DataFrame(np.vstack([f_value, y_hat, y]).T, columns=['f', 'y_hat', 'y']) # y는 실제값 
print(df.head(5))


# 평가지표
print()
print(confusion_matrix(y, y_hat))
# [[44  4]    TP  FN
#  [ 8 44]]   FP  TN

acc = (44+44)/ 100           # (TP + TN) / 전체수
recall = 44 / (44 + 4)       # TP / (TP + FN)
precision = 44 / (44 + 8)    # TP / (TP + FP)
specificity = 44 / (8+ 44)   # TN / (FP + TN) - 특이도
fallout = 8 / (8 + 44)       # FP / (FP + TN)

print('acc(정확도) : ', acc)
print('recall(재현율) : ', recall)     # TPR
print('precision(정밀도) : ', precision)
print('specificity(특이도) : ', specificity)
print('fallout(위양성률) : ', fallout)  # FPR
print('fallout(위양성률) : ', 1 - specificity)

print()
from sklearn import metrics
ac_sco = metrics.accuracy_score(y, y_hat)
print('ac_sco : ', ac_sco) # ac_sco :  0.88(정확도)

cl_rep = metrics.classification_report(y, y_hat)
print('cl_rep : ', cl_rep)

print('---- 정확도만 보고 땡치지 말고 분류결정 임계값(threshold)도 같이 보기 ----')
fpr, tpr, threshold = metrics.roc_curve(y, model.decision_function(x)) # (실제값, 판별함수)
print('fpr \n:', fpr)
print('tpr \n:', tpr)
print('분류결정 임계값(threshold) \n:', threshold) 
# 분류결정 임계값(threshold) : positive 예측값을 결정하는 확률 기준값

plt.plot(fpr, tpr, 'o-', label='Logistic Regression')
plt.plot([0,1], [0,1], 'k--', label='random classifier line(AUC:0.5)')
plt.plot([fallout], [recall], 'ro', ms=10) #위양성율, 재현률 
plt.xlabel('fpr')
plt.ylabel('tpr')
plt.title('ROC curve')
plt.legend()
plt.show()


#AUC : ROC 커브의 면적
print('AUC : ', metrics.auc(fpr, tpr)) # 1에 근사할수록 좋은 분류모델 AUC :  0.9547275



