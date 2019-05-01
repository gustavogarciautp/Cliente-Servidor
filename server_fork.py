import os
import time
import socket
import sys
import re

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(10)

def resta(connection, address):
    while True:
        res = "1|"
        data = connection.recv(1024)
        if data:
            a = data.split("|")
            if len(a) == 3:
                if a[0] != "-":
                    res+="Operador incorrecto"
                else:
                    patron = re.compile('^(-|\+)?[0-9]+(\.[0-9]+)?$')
                    ans = patron.match(a[1])
                    ans1 = patron.match(a[2])
                    if ans and ans1:
                        resta = float(a[1]) - float(a[2])
                        res = "0|Respuesta: " + str(resta)
                    else:
                        if not ans:
                            res += "operando 1 "
                        if not ans1:
                            res += "operando 2"
                        res=res.rstrip()
            else:
                res= "La expresion debe ser Operandor|Operando1|Operando2"
            connection.sendall(res)
        else:
            print >>sys.stderr, 'no more data from', address
            exit(0)
                

while True:
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    print >>sys.stderr, 'connection from', client_address

    pid = os.fork()

    if pid<0:
    	print >>sys.stderr, 'Error create process'
    elif pid==0:
    	resta(connection, client_address)
    else:
    	continue

connection.close()