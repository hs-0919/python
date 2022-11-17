# numpy
import numpy as np


ss =['tom','james','oscar', 1]
print(ss, type(ss))  # <class 'list'> 콤마 있음 - 리스트 

ss2 = np.array(ss)
print(ss2, type(ss2))  # <class 'numpy.ndarray'> 콤마 빼고 보여줌... - 넘파이
# 배열 - 요소의 타입이 일치해야 한다. ['tom' 'james' 'oscar' '1'] - 타입 일치시켜줌

# 메모리 비교 (list vs numpy)(빅데이터에서는 리스트 안씀)
li = list(range(1,11))
print(li)
print(li[0], li[1], id(li[0]), id(li[1]))  # 별도의 객체 주소를 기억
print(li * 10)

print("--------")
num_arr = np.array(li)
print(num_arr[0], num_arr[1], id(num_arr[0]), id(num_arr[1]))  # 배열의 요소들이 같은 주소를 기억.
print(type(num_arr), num_arr.dtype, num_arr.shape, num_arr.ndim, num_arr.size)
#ndim - 1차원, size - 요소 몇개야, shape- 차원크기
print(num_arr[1], ' ', num_arr[1:5])

print()
b = np.array([[1,2,3],[4,5,6]])
print(b.ndim)
print(b[0], b[0][0], b[[0]]) # 0행 0열 = 1 , [[0]] = 이차원?의 0번째

c = np.zeros((2,2))
print(c)

d = np.ones((2,2))
print(d)

e = np.full((2,2), fill_value = 7)
print(e)

f = np.eye(3) # 주대각만 1 나머지 0
print(f)

print()
np.random.seed(0)
print(np.random.rand(5))  # 균등분포
print(np.mean(np.random.rand(5)))

print(np.random.randn(5)) # 정규분포
print(np.mean(np.random.randn(5)))

print()
print(list(range(1, 10)))
print(np.arange(10))

print()
a = np.array([1,2,3,4,5])
print(a[1:4])
print(a[1:4:2])
print(a[1: ])
print(a[1:])
print(a[-4])

b = a
print(a)
print(b)
b[0] = 33 
print(a)
print(b)
c = np.copy(a)  # 복사본
c[0] = 77
print(a)
print(c)

print('-----------------')
a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a[:])
print(a[0], a[0][0], a[0])
print(a[[0][0]], a[0,0])
print(a[1, 0:2])

print()
print(a)
b =a[:2, 1:3]
print(b)
b[0,0] = 88
print(b)
print(a)

print()
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
r1 = a[1, :]   # 차원 축소
r2 = a[1:2, ]  # 차원 유지
print(r1, r1.shape)
print(r2, r2.shape)
# 슬라이싱으로 차원을 축소, 확대 할 수 있다.

print()
c1 =a[:, 1]
c2 =a[:, 1:2]
print(c1, c1.shape)
print(c2, c2.shape)

print()
bool_idx = (a > 5)
print(bool_idx)
print(a[bool_idx])
print(a[a > 5])


