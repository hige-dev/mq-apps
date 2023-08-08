#!/usr/bin/env python
import pika
from db import database

class RabbitMQ():
    def __init__(self):
        self.cred = pika.PlainCredentials('root', 'password')

    def __connection(self):
        return pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', 5672, '/', self.cred))

    def publish(self, exchange='', routing_key='', body=''):
        conn = self.__connection()
        channel = conn.channel()
        channel.queue_declare(queue=routing_key)
        channel.basic_publish(exchange=exchange,routing_key=routing_key,body=body)
        conn.close()

    def callback(self, ch, method, properties, body):
        sql = body.decode()
        print(f"Received: '{sql}'")
        self.__db_query_exec(sql)
        ch.basic_ack(delivery_tag = method.delivery_tag)

    def __db_query_exec(self, sql):
        db = database.Database()
        db.execute(sql)

    def consume(self):
        conn = self.__connection()
        channel = conn.channel()

        channel.basic_consume(
            queue = 'app',
            on_message_callback=self.callback,
            auto_ack=True
        )

        channel.start_consuming()

if __name__ == '__main__':
    mq = RabbitMQ()
    mq.consume()
