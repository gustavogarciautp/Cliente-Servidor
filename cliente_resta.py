import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port=raw_input("Ingrese puerto: ")
# Connect the socket to the port where the server is listening
server_address = ('192.168.0.13', int(port)) #esta es la direccion del servidor
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address) #establezco el conect con el socket

while True:
    try:
        message= raw_input("Mensaje: ")
        print >>sys.stderr, 'sending "%s"' % message
        sock.send(message)  #envia el mensaje
        data = sock.recv(1024) #tamano del buffer ddel servidor
        print >>sys.stderr, 'received "%s"' % data
    finally:
        pass
        #print >>sys.stderr, 'closing socket'
sock.close()

