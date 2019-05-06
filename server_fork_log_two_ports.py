import os
import time
import socket
import sys
import re
import time
import csv

ip= '192.168.0.13'

file = open ('log_server_recv.csv','a')
writer= csv.writer(file, delimiter=';')
file2 = open ('log_server_send.csv','a')
writer2= csv.writer(file2, delimiter=';')
file3 = open ('time_accept.csv','a')
writer3= csv.writer(file3, delimiter=';')
file4 = open ('time_request.csv','a')
writer4= csv.writer(file4, delimiter=';')

def resta(connection, address):
    while True:
        res = "1|"
        data = connection.recv(1024)
        start_time = time.time()
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
            exit(0)
        end_time = time.time()
        writer4.writerows([[end_time - start_time]])
        #print("Tiempo de respuesta: "+str(end_time - start_time))
                
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
            exit(0)


def accepting(sock, port):
    while True:
        try:
            print >>sys.stderr, 'waiting for a connection in port %d\n' % port
            connection, client_address = sock.accept()
            print >>sys.stderr, 'connection from', client_address
            start_time=time.time()

            pid = os.fork()

            if pid<0:
            	print >>sys.stderr, 'Error create process'
            elif pid==0:
                if port==10000:
            	   resta(connection, client_address)
                else:
                    info(connection, client_address)
            else:
            	end_time= time.time()
                writer3.writerows([[end_time - start_time]])
        except KeyboardInterrupt:
            sock.close()
            print("\nbye")
            break


if __name__ == '__main__':
    ports=[8000,10000]
    sockets=[]
    for i in range(2):
        # Create a TCP/IP socket
        sockets.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))

        # Bind the socket to the port
        server_address = (ip, ports[i])
        print >>sys.stderr, 'starting up on %s port %s' % server_address
        sockets[i].bind(server_address)

        # Listen for incoming connections
        sockets[i].listen(socket.SOMAXCONN)
    pid = os.fork()
    if pid<0:
        print >>sys.stderr, 'Error create process'
    elif pid==0:
        accepting(sockets[0], ports[0])
    else:
        accepting(sockets[1], ports[1])

    