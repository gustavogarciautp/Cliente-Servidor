import xmlrpclib
import socket
import sys
import random

proxy = xmlrpclib.ServerProxy("http://192.168.0.13:10000/")

for i in range(20):
        try:
            #message= raw_input("Mensaje: ")
            #print >>sys.stderr, 'sending "%s"' % message
            a = random.randint(1,1000)
            b = random.randint(1,1000)
            c = proxy.resta(a,b)
            print(c)
        except:
            pass

