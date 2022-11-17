# 웹 서버 구축

from http.server import SimpleHTTPRequestHandler, HTTPServer
# HTTPServer: 기본적인 socket 연결을 관리
# SimpleHTTPRequestHandler : 요청을 처리 (get, post)

port = 7777

handler =SimpleHTTPRequestHandler # SimpleHTTPRequestHandler - 단순서버 받는거만 된다
serv =HTTPServer(('127.0.0.1', port), handler)
print(' 웹서비스 시작!')
serv.serve_forever() # favicon.ico - 아이콘 같은거 안만들면 404지만 안만들어도 상관없다....



