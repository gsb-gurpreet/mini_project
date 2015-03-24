import socket #for sockets
import sys #for exit
 
# create dgram udp socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()

# the ip address to the beaglebone black is you want to use wifi use ifconfig onthe beaglebone to get the ip address
hostIP = '127.0.0.1'
port = 8888
 
while True:
    msg = raw_input('Enter message to send : ')

    try :
        #Set the whole string
        s.sendto(msg, (hostIP, port))
 
        # receive data from client (data, addr)
        d = s.recvfrom(1024)
        reply = d[0]
        addr = d[1]
 
        print 'Server reply : ' + reply
 
    except socket.error, msg:
        print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()