import pandas as pd
from pandas import Series, DataFrame
import numpy as np

obj= np.random.randn(9, 4)
print(obj)
print(DataFrame(obj, columns=['No1', 'No2', 'No3', 'No4']))
print(obj.mean(axis=0))
print()


obj1=pd.DataFrame([[i] for i in range(10, 41, 10)], columns=['numbers'], index=['a','b','c','d'])
print(obj1)
print()
print(obj1.iloc[2])


