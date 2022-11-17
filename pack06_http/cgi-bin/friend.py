import cgi

form = cgi.FieldStorage()

name = form["name"].value    # request.getpameter("name") : java 와 같다
phone = form["phone"].value
gen = form["gen"].value

print('Content-Type:text/html; charset=utf-8\n')
print('''
<html>
<body>

친구 이름은 {0}
<br>

전화는 {1}, 성별을 {2}

</body>
</html>
'''.format(name, phone, gen))



