#!/usr/bin/env python
import pika

class RabbitMQ():
    def __init__(self):
        self.cred = pika.PlainCredentials('root', 'password')

    def __connection(self):
        return pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', 5672, '/', self.cred))

    def publish(self, exchange='', routing_key='app', body=''):
        conn = self.__connection()
        channel = conn.channel()
        channel.queue_declare(queue=routing_key)
        channel.basic_publish(exchange=exchange,routing_key=routing_key,body=body)
        conn.close()
