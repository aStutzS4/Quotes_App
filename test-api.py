from flask import Flask, jsonify, request
import sqlite3
import records

app = Flask(__name__)
db = records.Database('sqlite:///quotes.db')
conn = sqlite3.connect('quotes.db', check_same_thread=False)
rows = db.query('select * from quotes')

@app.route('/test')
def test():
    db.query('Select * from quotes')
    return 'test'

#@app.router('/quote', methods = ['POST'])
#def add_quote():
   


app.run('0.0.0.0', debug=True)
