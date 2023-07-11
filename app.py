from flask import Flask, request, json
from flask_sqlalchemy import SQLAlchemy
import leveldb

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:////tmp/test.db'
sql_db = SQLAlchemy(app)
utxo_db = leveldb.LevelDB('utxo', create_if_missing=True)
spent_utxo_db = leveldb.LevelDB('spent_utxo', create_if_missing=True)
block_db = leveldb.LevelDB('block', create_if_missing=True)


class User(sql_db.Model):
    email = sql_db.Column(sql_db.String(40), primary_key=True)
    passwd = sql_db.Column(sql_db.String(40), unique=False, nullable=False)
    accountAddress = sql_db.Column(sql_db.String(100), unique=True, nullable=False)
    userPubKey = sql_db.Column(sql_db.String(400), unique=True, nullable=False)
    userSignKey = sql_db.Column(sql_db.String(400), unique=True, unllable=False)


@app.route('/test', methods=['POST', 'GET'])
def test_connection():
    key = request.json['key']
    value = request.json['value']
    utxo_db.Put(key.encode(), value.encode())
    print(utxo_db.Get(key.encode()).decode())
    return "success!!"


@app.route('/signup', method=['POST', 'GET'])
def user_signup():
    email = request.json['email']
    passwd = request.json['passwd']
    gruut_address = request.json['address']
    public_key = request.json['publicKey']


if __name__ == "__main__":
    app.run(host="192.168.129.134", port=5000)
