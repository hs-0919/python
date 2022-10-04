# 집합 자료형 : str, list, typle, set, dict

# 문자열 : str - 순서 o: 인덱싱(하나의 값만 참조), 슬라이싱(여러값 참조)이 가능 , 수정 x  

s='sequence'
print(s, type(s), len(s))
print(s.count('e'))
print(s.find('e'), '', s.find('e',3), s.rfind('e'))# rfind- 뒤에서부터
#...


# 수정 불가
ss='mbc'
print(ss, id(ss))
ss='abc'
print(ss, id(ss))

#인덱싱,  슬라이싱  대상[start:stop:step]
print(s[0], s[3]) # s[8] err남
print(s[-1], s[-3])

print(s[0:3], s[3:], s[:3], s[:], s[1:5:2], s[::2]) 
#0 이상 3 미만, 3자리 이후로, 3자리 까지, 몽땅 다, 1이상 5미만 증가치2, 모든 글자에서 2번째는 빼고 
print(s[-4:-1], s[-3:])
print('fre' + s[2:]) # 일부의 값만 참조
print()

s2='kbs mbc'
s2=' ' + s2[:4] + 'sbs ' + s2[4:] + ' '
print(s2, len(s2))
print(s2.strip()) #lstrip(), rstrip()

s3=s2.split(sep=' ') #split - 자르는거
print(s3)
print(':'.join(s3)) #join - 집합형

a='life is too long'
b=a.replace('life', 'Your leg')
print(b)

