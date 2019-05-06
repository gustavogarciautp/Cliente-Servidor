import os
import time
import socket
import sys
import re
import time
import csv
import threading

ip= '192.168.0.13'
flag = 0
clock = 0

file = open ('log_server_recv.csv','a')
writer= csv.writer(file, delimiter=';')
file2 = open ('log_server_send.csv','a')
writer2= csv.writer(file2, delimiter=';')

def resta(connection, address):
    while True:
        res = "1|"
        data = connection.recv(1024)
        if data:
            print(data)
            writer.writerows([[data]])
            #time.sleep(60)
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
            connection.sendall(res)
            writer2.writerows([[address[0],address[1],data,res]])
        else:
            print >>sys.stderr, 'no more data from', address
            break

def info(connection, address):
    while True:
        data = connection.recv(1024)
        if data:
            if data=="Sv?":
                res= 'Serv|-|10000'
            else:
                res= 'Solicitud incorrecta'
            connection.sendall(res)
        else:
            print >>sys.stderr, 'no more data from', address
            break


def accepting(sock, port):
    threads=[]
    while True:
        try:
            print >>sys.stderr, 'waiting for a connection in port %d\n' % port
            connection, client_address = sock.accept()
            print >>sys.stderr, 'connection from', client_address
            time.sleep(60)
            if port==10000:
                thread = threading.Thread(target = resta, args = (connection, client_address))
                thread.setDaemon(True)
                threads.append(thread)
                thread.start()
            elif port == 8000:
                thread = threading.Thread(target = info, args = (connection, client_address))
                threads.append(thread)
                thread.setDaemon(True)
                thread.start()
            else:
            	continue
        except KeyboardInterrupt:
            sock.close()
            print("\nbye")
            break


if __name__ == '__main__':
    
    ports=[8000,10000]
    sockets = []
    for i in range(2):
        # Create a TCP/IP socket
        sockets.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) 
        # Bind the socket to the port
        #print(sockets[i].getsockname())
        server_address = (ip, ports[i])
        print >>sys.stderr, 'starting up on %s port %s' % server_address
        sockets[i].bind(server_address)
        # Listen for incoming connections
        sockets[i].listen(socket.SOMAXCONN)

    thread = threading.Thread(target=accepting, args = (sockets[0], ports[0]))
    thread.setDaemon(True)
    thread.start()

    accepting(sockets[1], ports[1])
    print("Server down")

