import sys
import random
import threading
import csv
import xmlrpclib


file = open ('log_client_send_recv.csv','a')
writer= csv.writer(file, delimiter=';')

def solicitudes(proxy):
    for i in range(10):
        a = random.randint(1,1000)
        b = random.randint(1,1000)

        c = proxy.resta(a,b)            
        writer.writerows([[a,b,c]])
        print(c)

def main():
    threads=list()
    for i in range(35):
        proxy = xmlrpclib.ServerProxy("http://192.168.0.13:10000/")
        thread= threading.Thread(target=solicitudes, args=(proxy,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main()
    file.close()

