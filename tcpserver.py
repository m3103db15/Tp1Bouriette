from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(1)

serverPort2 = 10000
serverSocket2 = socket(AF_INET,SOCK_STREAM)

print "The server is ready to receive"
while 1:
	connectionSocket, addr = serverSocket.accept()
	sentence = connectionSocket.recv(1024)
	capitalizedSentence = sentence.upper()
	print "From Server:", capitalizedSentence
	connectionSocket.close()
	serverSocket2.bind("",serverPort2))
serverSocket.2listen(1)

while 2:
	connectionSocket, addr = serverSocket2.accept()
	connectionSocket.send(capitalizedSentence)
	print "From Server:", capitalizedSentence
	connectionSocket.close()
