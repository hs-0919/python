# DataFrame의 재구조화 : stack/unstack

import pandas as pd
import numpy as np


df = pd.DataFrame(1000 + np.arange(6).reshape(2,3),
                  columns=['2020','2021','2022'], index=['대전','서울'])

print(df)

print()
df_row = df.stack()  # index를 기준으로 열 쌓기, 열을 인덱스로 가져옴, 구조를 바꿈
print(df_row)

print()
df_col = df_row.unstack()  # stack 결과 원복, 인덱스를 열로 보내는 역할
print(df_col)

print('데이터 범주화 (연속형 데이터 ==> 범주형)--------------------')
price = [10.3, 5.5, 7.8, 3.6]
cut = [3, 7, 9, 11]  # 구간 기준 값
result_cut = pd.cut(price, cut)
print(result_cut)  # (9, 11] - 9보다 크고 11보다 작거나 같은거
print(pd.value_counts(result_cut))

print()
datas = pd.Series(np.arange(1, 1001))
print(datas)
print(datas.head(2))
print(datas.tail(2))

cut2 = [1, 500, 700, 1000]  # 구간 기준 값
result_cut2 = pd.cut(datas, cut2)
print(result_cut2)

print()
result_cut2 = pd.qcut(datas, 3)
print(result_cut2)
print(pd.value_counts(result_cut2))

print()
# 각 범주의 그룹별 연산
group_col = datas.groupby(result_cut2)
print(group_col.agg(['count', 'mean','std','min'])) # 그룹 집계 함수

# 직접 함수 작성
def summary_func(gr):
    return{
        'count':gr.count(),
        'mean':gr.mean(),
        'std':gr.std(),
        'min':gr.min()
    }
print(group_col.apply(summary_func))
print(group_col.apply(summary_func).unstack())

