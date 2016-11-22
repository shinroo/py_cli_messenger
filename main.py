from socket import *
import thread
import time

BUFFERSIZE = 1024
HOST = '127.0.0.1'
PORT = 8080

def receiver(clientsock,addr):
	data = clientsock.recv(BUFFERSIZE)
	print 'received from ' + addr[0] + ':' + addr[1] + ': '  + repr(data)
	clientsock.send('')
	clientsock.close()

def receiver_thread():
	ADDR = (HOST, PORT)
	serversock = socket(AF_INET, SOCK_STREAM)
	serversock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	serversock.bind(ADDR)
	serversock.listen(5)
	while 1:
		print 'waiting for conenction...'
		clientsock, addr = serversock.accept()
		print 'got connection from: ', addr
		thread.start_new_thread(receiver, (clientsock, addr))

def sender(hostname, port, message):
	sendsock = socket(AF_INET, SOCK_STREAM)
	sendsock.connect((hostname, port))
	sendsock.send(message)
	sendsock.close()

######

thread.start_new_thread(receiver_thread, ())
while 1:
	message = raw_input("waiting for message:")
	sender(HOST, PORT, message)
