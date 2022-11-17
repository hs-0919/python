# 웹 서버 구축

from http.server import CGIHTTPRequestHandler, HTTPServer
# CGIHTTPRequestHandler - 동적으로 웹서버를 운영가능하게 해준다.
# CGI - 웹서버와 외부 프로그램 사이에서 정보를 주고 받는 방법 또는 규약, 약속

port = 8888
class Handler(CGIHTTPRequestHandler):
    cg_directories = ['/cgi-bin']
    
serv =HTTPServer(('127.0.0.1', port), Handler)
print(' 웹서비스 시작!')
serv.serve_forever() # favicon.ico - 아이콘 같은거 안만들면 404지만 안만들어도 상관없다.... 
    










