import sys
import socket

address = sys.argv[1]
port_number = int(sys.argv[2])

print((address))
print(port_number)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((address,port_number))

s.close()

import threading

def reciving():
	print s.recv(1024)

def sending():
	s.send(str(input());

threadobj = threading.Thread(target=reciving)
threadobj2 = threading.Thread(target=sending)

threadobj.start()
threadobj2.start()
