"""
    http请求响应演示
"""

from socket import *

s = socket()
s.bind(("0.0.0.0",8000))
s.listen(3)

c,addr=s.accept()
print("connect from",addr)

data=c.recv(2048)
print(data.decode())

# 组织http相应的格式发送
http_data = """HTTP/1.1 200 OK
Content-Type:text/html

"""
c.send(http_data.encode())
f=open("index.html",'r')
while True:
    data=f.read(1024)
    if not data:
        break
    c.send(data.encode())

c.close()
s.close()


