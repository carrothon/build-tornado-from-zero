#coding:utf-8
import socket
from time import ctime

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = ('127.0.0.1', PORT)

# 服务器端创建 socket
serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSock.bind(ADDR)
serverSock.listen(5)

while True:
	server2client_Sock, addr = serverSock.accept()

	while True:
		data = server2client_Sock.recv(BUFSIZE)

		# 如果数据接收完，则退出 recv, 进入到下一个连接
		if not data:
			break

		server2client_Sock.send('[%s] %s' % (ctime(), data))

	server2client_Sock.close()

serverSock.close()