#!/usr/bin/env python
import pika
import re
import time
import csv

credentials = pika.PlainCredentials('gus2', 'man1')
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.0.20',10000, '/', credentials))

channel = connection.channel()

channel.queue_declare(queue='resta_queue')

def on_request(ch, method, props, body):
    res = "1|"
    data=body.decode("UTF-8")
    print("Received" +data)
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

    ch.basic_publish(exchange='',routing_key=props.reply_to,properties=pika.BasicProperties(correlation_id = props.correlation_id),body=str(res))
    ch.basic_ack(delivery_tag=method.delivery_tag) #envia un reconocimiento, una vez que hayamos terminado con una tarea.

#channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='resta_queue', on_message_callback=on_request)

print("Awaiting requests")
channel.start_consuming()