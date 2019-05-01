import socket
import sys
import random

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000) #esta es la direccion del servidor
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address) #establezco el conect con el socket

for i in range(500):
    try:
        #message= raw_input("Mensaje: ")
        #print >>sys.stderr, 'sending "%s"' % message
        a = random.randint(1,1000)
        b = random.randint(1,1000)
        #print(a)
        #print(b)
        message = "-" + "|" + str(a) + "|" + str(b)
        sock.send(message)  #envia el mensaje
        data = sock.recv(1024) #tamano del buffer ddel servidor
        print >>sys.stderr, 'received "%s"' % data
    finally:
        pass
    #print >>sys.stderr, 'closing socket'
sock.close()

