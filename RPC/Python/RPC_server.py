import socket
import sys
import threading
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer

host = "192.168.0.13"

def info(connection, address):
    while True:
        data = connection.recv(1024)
        if data:
            if data=="Sv?":
                res= 'Serv|-|10000|resta'
            else:
                res= 'Solicitud incorrecta'
            connection.sendall(res)
        else:
            print('no more data from'+ str(address))
            break

def resta(op1, op2):
    print("Resta "+str(op1)+" - "+str(op2))
    #time.sleep(10)
    return op1-op2

def accepting():
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host,8000))
    sock.listen(socket.SOMAXCONN)
    while True:
        try:
            print('waiting for a connection in port 8000')
            connection, client_address = sock.accept()
            print('connection from '+str(client_address))
            thread = threading.Thread(target = info, args = (connection, client_address))
            thread.setDaemon(True)
            thread.start()
        except KeyboardInterrupt:
            sock.close()
            print("\nbye")
            break


server = SimpleXMLRPCServer((host, 10000))
server.register_function(resta, "resta")

thread = threading.Thread(target=accepting)
thread.setDaemon(True)
thread.start()
print("server conect")
server.serve_forever()

