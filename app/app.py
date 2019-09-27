import datetime
import os

import pymysql
from flask import Flask
from flask import jsonify

app = Flask(__name__)


class Database:
    def __init__(self):
        host = os.getenv('DB_HOST', 'localhost')
        user = os.getenv('DB_USER', 'root')
        password = os.getenv('DB_PASS', 'root')
        port = int(os.getenv('DB_PORT', 3306))
        db = 'desafio'
        self.connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db,
            port=port,
            cursorclass=pymysql.cursors.DictCursor,
        )
        self.cursor = self.connection.cursor()

    def list_messages(self):
        self.cursor.execute('SELECT id, message FROM revistas')
        return self.cursor.fetchall()


@app.route('/', methods=['GET'])
def index():
    db = Database()
    messages = db.list_messages()
    return jsonify(messages)


@app.route('/time', methods=['GET'])
def time():
    return '{date}'.format(date=datetime.datetime.now())


if __name__ == '__main__':
    app.run(host='0.0.0.0')
