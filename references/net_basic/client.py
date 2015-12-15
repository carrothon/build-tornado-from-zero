#coding:utf-8
import socket
from time import ctime

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

# 客户端创建 socket
clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSock.connect(ADDR)


while True:
	data = raw_input("> ")
	if not data:
		break

	clientSock.send(data)

	recData = clientSock.recv(BUFSIZE)
	if not recData:
		break

	print recData

clientSock.close()

	