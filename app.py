from flask import Flask, request, json
import leveldb

app = Flask(__name__)

utxo_db = leveldb.LevelDB('utxo', create_if_missing=True)
spent_utxo_db = leveldb.LevelDB('spent_utxo', create_if_missing=True)
block_db = leveldb.LevelDB('block', create_if_missing=True)


@app.route('/test', methods=['POST', 'GET'])
def test_connection():
    key = request.json['key']
    value = request.json['value']
    utxo_db.Put(key.encode(), value.encode())
    print(utxo_db.Get(key.encode()).decode())
    return "success!!"


if __name__ == "__main__":
    app.run(host="192.168.129.134", port=5000)
