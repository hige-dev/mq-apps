from flask import Flask, request
from db import database
import random

app = Flask(__name__)

@app.route('/')
def index():
    return "publish to RabbitMQ"

@app.route('/users', methods=["GET"])
def show_all():
    db = database.Database()
    return db.execute('select * from users;')

@app.route('/users', methods=["POST"])
def create():
    db = database.Database()
    name = request.get_data().decode() or 'asd'
    for i in range(0, random.randint(0,10)):
        db.execute(f'insert into users (name) values (\'{name}{i}\');')
    return 'ok'

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
