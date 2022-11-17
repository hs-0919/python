# 웹 서비스 대상 파일
# print() -> 브라우저에게 전송한다는 의미 /

kor = 50
eng = 60
tot = kor + eng



print('Content-Type:text/html; charset=utf-8\n')  # Content-Type:text/html -> MIME TYPE이다.
print('<html><body>')
print('<b>안녕 지옥이야</b> 파이썬 모듈로 작성했어<br>')
print('총점은 %s'%(tot))
print('</body></html>')





















