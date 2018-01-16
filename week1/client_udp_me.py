import socket
"""
while(1):
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


	s.sendto("jp you are the thop",("10.64.1.173",8005))
	print s.recvfrom(1024)

	s.close()
"""
import threading

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
def reciving():
        fp = open("file.txt","a")		
	while(1):
                fp = open("file.txt","a")		
		x,address = s.recvfrom(1024)
		fp.write(x)
		print(x)
		fp.close()
def sending():
	while(1):
		s.sendto(str(raw_input()),("10.64.1.173",8005))

threadobj = threading.Thread(target=reciving)
threadobj2 = threading.Thread(target=sending)

threadobj.start()
threadobj2.start() 
