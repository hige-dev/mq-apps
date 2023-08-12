#!/usr/bin/env python
import pika
from db import database

class RabbitMQ():
    def __init__(self):
        self.cred = pika.PlainCredentials('root', 'password')

    def __connection(self):
        return pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', 5672, '/', self.cred))

    def callback(self, ch, method, properties, body):
        sql = body.decode()
        print(f"Received: '{sql}'")
        self.__db_query_exec(sql)

    def __db_query_exec(self, sql):
        db = database.Database()
        db.execute(f'insert into users (name) values (\'{sql}\')')

    def consume(self):
        conn = self.__connection()
        channel = conn.channel()
        channel.queue_declare(queue='app')
        channel.basic_consume(
            queue = 'app',
            on_message_callback=self.callback,
            auto_ack=True
        )

        channel.start_consuming()

if __name__ == '__main__':
    mq = RabbitMQ()
    mq.consume()
