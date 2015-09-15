import socket
import sys
import time
import threading

s = socket.socket()
host = '192.168.0.3'
port = 6005




s.connect((host, port))

print(s.recv(1024).decode('ascii'))

cont2 = True

def sender():

	time.sleep(.1)
	print('t1 test')
	cont1 = True
	global cont2

	while cont1:
		output = input()
		
		if output == 'stop':
			s.send(output.encode('ascii'))
			print('attempting to stop')
			cont1 = False
			cont2 = False
			
		else:
			s.send(output.encode('ascii'))
		time.sleep(.1)
			
def receiver():

	time.sleep(.2)
	print('t2 test')

	global cont2

	while cont2:
		print(s.recv(1024).decode('ascii'))
		time.sleep(.1)
		
t1 = threading.Thread(target=sender, args=())
t2 = threading.Thread(target=receiver, args=())

t1.start()
t2.start()

print('y0')

t1.join()
t2.join()

s.close()
