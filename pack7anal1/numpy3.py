# 배열 연산
import numpy as np

x =np.array([[1,2],[3,4]], dtype=np.float64)
print(x, x.dtype)

y =np.arange(5, 9).reshape(2,2) # 1차원 -> 2차원
y = y.astype(np.float64)
print(y, y.dtype)

print()
print(x + y)
print(np.add(x,y))   # 결과는 같다
imsi = np.random.rand(10000)
print(imsi)
print(sum(imsi))
print(np.sum(imsi)) # 결과는 같다, 파이썬 연산함수보다 속도가 빠름

print()
print(x-y)
print(np.subtract(x,y))

print()
print(x*y)
print(np.multiply(x,y))

print()
print(x/y)
print(np.divide(x,y))

print()
# 백터 간 내적 연산 : dot 참고로 r에서는 a%*%b
v = np.array([9, 10])
w = np.array([11, 12])
print(v * w)
print(v.dot(w))  # v[0]*w[0] + v[1]*w[1]
print(np.dot(v,w))

print()
print(x)
print(v)
print(np.dot(x,v))  # x[0][0]*v[0] + x[0][1]*v[1] = 29, x[1][0]*v[0] + x[1][1]*v[1] = 67

print()
print(x)
print(y)
print(np.dot(x,y))  # x[0,0]*y[0,0] + x[0,1]*y[1,0] = 29

print('-----------------')
print(np.sum(x))
print(np.mean(x))
print(np.cumsum(x))  # 누적합
print(np.cumprod(x)) # 누적곱


print()
name1 = np.array(['tom','james','tom','oscar'])
name2 = np.array(['tom','page','john'])
print(np.unique(name1))  # 중복 배제
print(np.intersect1d(name1, name2, assume_unique=True))  # 교집합, assume_unique=True -> 중복 허용
print(np.union1d(name1, name2))  # 합집합
 
print('\nTranspose : 전치')
print(x)
print(x.T)
print(x.transpose())
print(x.swapaxes(0,1))

print('\nBroadcast 연산 : 크기가 다른 배열 간의 연한을 하면 작은 배열이 큰 배열의 크기를 자동으로 따라감')
x = np.arange(1,10).reshape(3,3)
print(x)
y = np.array([1,0,1])
print(x+y)

print()
print(x)
np.savetxt('my.txt', x)
imsi = np.loadtxt('my.txt')
print(imsi)
print()
imsi2 = np.loadtxt('my2.txt', delimiter=',')
print(imsi2)


