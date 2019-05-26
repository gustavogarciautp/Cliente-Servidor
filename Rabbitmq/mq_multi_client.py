#!/usr/bin/env python
import pika
import uuid
import random
import threading
import csv

file = open ('log_client.csv','a')
writer= csv.writer(file, delimiter=';')


class Resta_Client(object):

    def __init__(self):
        self.credentials= pika.PlainCredentials('gus2', 'man1')
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.0.20',10000,'/',self.credentials))

        self.channel = self.connection.channel()

        #creamos una sola cola de devolución de llamada por cliente
        result = self.channel.queue_declare('', exclusive=True)  #una vez que se cierra la conexión del consumidor, la cola se debe eliminar.


        self.callback_queue = result.method.queue  #el servidor elije un nombre de cola aleatorio para nosotros, result.method.queue contiene ese nombre

        self.channel.basic_consume(queue=self.callback_queue, on_message_callback=self.on_response,auto_ack=True) # los acuses de recibo los desactivamos explícitamente mediante el indicador auto_ack = True

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        # correlation_id es útil para correlacionar respuestas con solicitudes. Es un valor unico para cada solicitud,
        self.channel.basic_publish(exchange='',routing_key='resta_queue', properties=pika.BasicProperties(reply_to=self.callback_queue,correlation_id=self.corr_id),body=n)
        while self.response is None:
            self.connection.process_data_events()
        return self.response.decode("UTF-8")


def requests(id_,obj_client):
    for i in range(20):
        a = random.randint(1,1000)
        b = random.randint(1,1000)
        message="-" + "|" + str(a) + "|" + str(b)
        print(message)
        response = obj_client.call(message)
        writer.writerows([[id_,message,response]])
        print(response)

threads=list()
for i in range(10):
    client = Resta_Client()
    thread= threading.Thread(target=requests, args=(i,client))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()


