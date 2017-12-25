from flask import Flask, jsonify, request
import records

app = Flask(__name__)

db = records.Database('sqlite:///quotes.db')

@app.route('/quotes')
def get_quotes():
    rows = db.query('select * from quotes')
    return jsonify(rows.as_dict())

@app.route('/quotes/random')
def get_random_quote():
    row = db.query('select * from quotes order by RANDOM() LIMIT 1')
    return jsonify(row.as_dict())

@app.route('/quotes', methods = ['POST'])
def add_quote():
    data = request.get_json()
    print(data)
    db.query('insert into quotes (text) values (:text)', text=data['text'])
    return 'Created', 201

@app.route('/quotes/<int:id>', methods = ['DELETE'])
def remove_quote(id):
    db.query(f'Delete from quotes where id = {id}')
    return 'OK', 200

app.run('0.0.0.0') 

