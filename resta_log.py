import socket
import threading
import sys
import re
import csv

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(20)

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
                res= "La expresion debe ser Operador|Operando1|Operando2"
            file = open ('log_thread.csv','a')
            writer= csv.writer(file, delimiter=';')
            writer.writerows([[address[0],address[1],data,res]])
            file.close()
            connection.sendall(res)
        else:
            print >>sys.stderr, 'no more data from', address
            break
                

while True:
    try:
        print >>sys.stderr, 'waiting for a connection'
        connection, client_address = sock.accept()

        hilo=threading.Thread(target=resta, args=(connection,client_address))
        hilo.start()

        print >>sys.stderr, 'connection from', client_address
    except KeyboardInterrupt:
        print("bye")
        break

connection.close()