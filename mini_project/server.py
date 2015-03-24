import socket
import sys

HOST = "127.0.0.1"	#'' # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port

import time
#reduces parenthesis in the function codes
def off():
	print "Lights Out"

def red():
	print "Red On"

def green():
	print "Green On"

def blue():
	print "Blue On"

def yellow():
	print "Yello ON"

# Datagram (udp) socket
try :
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	print 'Socket created'
except socket.error, msg :
	print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
	sys.exit()
	 
# Bind socket to local host and port
try:
	s.bind((HOST, PORT))
except socket.error , msg:
	print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
	sys.exit()
print 'Socket bind complete'
	 
#now keep talking with the client
while True:
	    # receive data from client (data, addr)
	d = s.recvfrom(1024)
	data = d[0]
	addr = d[1]

	if not data:
		break
	reply = 'OK...' + data	 

# if the message is quit close the socket and exit script
	if data.find('quit') != -1:
		print 'quiting now!'
#send a message back saying the server is exiting
		s.sendto("server exiting now",addr)
		s.close()
		sys.exit()
	 
# if the message is off call the off method
	elif data.find('off') != -1:
		off()
	        #send a message back saying the lights are off
		s.sendto("Lights Out",addr)
		 
# if the message is red call the red method
	elif data.find('red') != -1:
		red()
	        #send a message back saying the red light is on
		s.sendto("Red On",addr)
		 
# if the message is green call the green method
	elif data.find('green') != -1:
		green()
	        #send a message back saying the green light is on
		s.sendto("Green On",addr)
		 
# if the message is blue call the blue method
	elif data.find('blue') != -1:
		blue()
	        #send a message back saying the blue light is on
		s.sendto("Blue On",addr)
		 
# if the message is yellow call the yellow method
	elif data.find('yellow') != -1:
		yellow()
	        #send a message back saying the yellow light is on
		s.sendto("Yellow On",addr)
	else:
		s.sendto(reply , addr)
	print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip()
		     
s.close()
