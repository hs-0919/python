# 한글 형태소 지원 라이브러리 konlpy를 사용
# 5언 9품사로 한글 문서를 분리
from konlpy.tag import Kkma, Okt
from konlpy.tag._komoran import Komoran 

 

kkma = Kkma()
print(kkma.sentences('한글 데이터 형태소 분석을 위한 라이브러리 설치를 합니다. 행운을 비빕니다.'))# 문장 단위
print(kkma.nouns('한글데이터형태소분석을위한라이브러리설치를합니다. 행운을 비빕니다')) # 명사만 
print(kkma.pos('한글데이터형태소분석을위한라이브러리설치를합니다. 행운을 비빕니다')) # 품사 태깅(품사 부착)
print(kkma.morphs('한글데이터형태소분석을위한라이브러리설치를합니다. 행운을 비빕니다')) # 모든 품사

print()
okt = Okt()
print(okt.phrases('한글 데이터 형태소 분석을 위한 라이브러리 설치를 합니다. 행운을 비빕니다.'))# 모든 품사
print(okt.nouns('한글데이터형태소분석을위한라이브러리설치를합니다. 행운을 비빕니다')) # 명사만 
print(okt.pos('한글데이터형태소분석을위한라이브러리설치를합니다. 행운을 비빕니다')) # 품사 태깅(품사 부착)
print(okt.morphs('한글데이터형태소분석을위한라이브러리설치를합니다. 행운을 비빕니다')) # 모든 품사


print()
komo = Komoran()
print(komo.nouns('한글데이터형태소분석을위한라이브러리설치를합니다. 행운을 비빕니다')) # 명사만 
print(komo.pos('한글데이터형태소분석을위한라이브러리설치를합니다. 행운을 비빕니다')) # 품사 태깅(품사 부착)
print(komo.morphs('한글데이터형태소분석을위한라이브러리설치를합니다. 행운을 비빕니다')) # 모든 품사










