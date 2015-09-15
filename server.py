import socket
import sys
import time
import threading

print('Greetings')

host = ''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.0.3'
port = 6005
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))

s.listen(5)




c, address = s.accept()
print('Got connection from ', address)
c.send('Thank you for connecting'.encode('ascii'))

cont = True
output = ''

def sender():
	global cont
	global output
	while cont == True:
		output = input()
		c.send(output.encode('ascii'))
		time.sleep(.1)
	print('Test')


def receiver():
	cont2 = True
	global cont
	
	while cont2 == True:
		client_output = c.recv(2048).decode('ascii')
		if client_output == 'stop':
			print('Press any key and hit enter to exit')
			cont = False
			cont2 = False
			
		else:
			print(client_output)
		time.sleep(.1)
	print('Test')
			


t1 = threading.Thread(target=sender, args=())
t2 = threading.Thread(target=receiver, args=())

t1.start()
t2.start()

t1.join()
t2.join()

c.close()
