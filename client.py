from socket import *


#specify nicnkame

NICKNAME = b"Bobek"

#specify the host and port

HOST = "localhost"
PORT = 8123


connection = socket()

try:
	connection.connect((HOST, PORT))
except ConnectionRefusedError:
	print("ERROR: Couldn't connect, host is down?")
	exit(0)


connection.send(NICKNAME)

while True:
	command = connection.recv(1024)

	print(command)

	if(command == b"WAKEUP"):
		connection.send(b"READY")


