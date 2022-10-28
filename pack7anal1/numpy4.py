# 배열에 행/열 추가
import numpy as np

aa = np.eye(3)
print(aa, aa.shape)

# 열 추가
bb= np.c_[aa, aa[2]]
print(bb)

# 행 추가
cc = np.r_[aa, [aa[2]]]
print(cc)

print()
a = np.array([1,2,3])
print('a = ', a)
print(np.c_[a]) # 차원이 확대, 행을 열로 변환
print(a.reshape(3,1))


print('------ append, insert, delete------')
print(a)
# b= np.append(a, [4,5])
b = np.append(a, [4, 5], axis=0) # axis = 0 열방향 1
print(b)

c = np.insert(a, 1, [6,7], axis=0)
print(c)

# d = np.delete(a,1)
# d = np.delete(a,[1])
d = np.delete(a,[1, 2])

print('------2차원------')
aa= np.arange(1, 10).reshape(3,3)
print(aa)
print(np.insert(aa, 1, 99))  # 차원 축소, aa배열을 차원 축소 후 1번째 지점에 99를 추가
print(np.insert(aa, 1, 99, axis=0)) # 행기준
print(np.insert(aa, 1, 99, axis=1)) # 열기준

print()
print(aa)
bb = np.arange(10, 19).reshape(3, 3)
print(bb)

cc = np.append(aa, bb)
print(cc)

cc = np.append(aa, bb, axis = 0)
print(cc)

cc = np.append(aa, bb, axis = 1)
print(cc)

print(np.delete(aa, 1))
print(np.delete(aa, 1, axis=0))
print(np.delete(aa, 1, axis=1))


