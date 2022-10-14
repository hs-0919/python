s1 = '자료1'
s2 = '자료2'
print('Content-Type:text/html; charset=utf-8\n')
print('''
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>안녕</h1>
자료 출력 : {0}, {1}

<br>
<img src='../images/다음로고.png' width='60%' />
<br/>
<a href='../index.html'>메인으로</a>
</body>
</html>

'''.format(s1,s2))


























