#!/usr/bin/env python
import pika
import db.database as db

class RabbitMQ():
    def __init__(self):
        self.cred = pika.PlainCredentials('root', 'password')

    def connection(self):
        return pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', 5672, '/', self.cred))

    def publish(self, exchange='', routing_key='', body=''):
        conn = self.connection()
        channel = conn.channel()
        channel.queue_declare(queue=routing_key)
        channel.basic_publish(exchange=exchange,routing_key=routing_key,body=body)
        conn.close()

    def callback(self, ch, method, properties, body):
        print("Received: '{}'".format(body))
        self.__db_query_exec(body)
        ch.basic_ack(delivery_tag = method.delivery_tag)

    def __db_query_exec(self, body):
        db = db.Database()
        db.execute(body)

    def consume(self):
        conn = self.connection()
        channel = conn.channel()

        channel.basic_consume(
            queue = 'app',
            on_message_callback=self.callback
        )

        channel.start_consuming()

