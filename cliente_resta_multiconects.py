import socket
import sys
import random
import threading
import csv

file = open ('log_client_send.csv','a')
writer= csv.writer(file, delimiter=';')

file2 = open ('log_client_recv.csv','a')
writer2= csv.writer(file2, delimiter=';')

def solicitudes(sock, id_):
    for i in range(2):
        try:
            #message= raw_input("Mensaje: ")
            #print >>sys.stderr, 'sending "%s"' % message
            a = random.randint(1,1000)
            b = random.randint(1,1000)
            #print(a)
            #print(b)
            message = "-" + "|" + str(a) + "|" + str(b)
            sock.send(message)  #envia el mensaje
            writer.writerows([[id_,i,message]])

            data = sock.recv(1024) #tamano del buffer ddel servidor
            if data:
                writer2.writerows([[id_,i,data]])
            #print >>sys.stderr, 'received "%s"' % data
        except:
            pass
    print >>sys.stderr, 'closing socket'
    sock.close()

def main():
    threads=list()
    for i in range(10):
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        server_address = ('192.168.0.13', 10000) #esta es la direccion del servidor
        print >>sys.stderr, 'connecting to %s port %s' % server_address
        sock.connect(server_address) #establezco el conect con el socket
        thread= threading.Thread(target=solicitudes, args=(sock,i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main()
    file.close()
    file2.close()

