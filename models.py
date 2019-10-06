import os
from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)

user = os.environ['POSTGRES_USER ']
pw = os.environ['POSTGRES_PW ']
url = os.environ['POSTGRES_URL ']
db = os.environ['POSTGRES_DB']
connect = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}' # .format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)

app.config['SQLALCHEMY_DATABASE_URI'] = connect
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning

db = SQLAlchemy(app)

class Balances(db.Model):
    __tablename__ = 'balances'
    id = db.Column(db.Integer, primary_key = True)
    address = db.Column(db.Text)
    balance = db.Column(db.Float)
    block = db.Column(db.Integer)
    txid = db.Column(db.Text)

    def __init__(self, address, amount, input, block, txid):
        self.address = address
        self.amount = amount
        self.input= input
        if self.input:
            self.balance = self.balance - self.amount
        else:
            self.balance = self.balance + self.amount
        self.block = block
        self.txid = txid

    def __repr__(self):
        cadena = f'Address {self.address} has a balance of {self.balance}'
        cadena += f'Last Block is {self.block} and last transaction is {self.txid}'

class Transactions(db.Model):
    __tablename__ = 'transactions'
    id = db.Column(db.Integer, primary_key = True)
    address = db.Column(db.Text)
    balance = db.Column(db.Float)
    block = db.Column(db.Integer)
    txid = db.Column(db.Text)

    def __init__(self, address, amount, input, block, txid):
        self.address = address
        self.amount = amount
        self.input= input
        if self.input:
            self.balance = self.balance - self.amount
        else:
            self.balance = self.balance + self.amount
        self.block = block
        self.txid = txid

    def __repr__(self):
        cadena = f'Address {self.address} has a balance of {self.balance}'
        cadena += f'Last Block is {self.block} and last transaction is {self.txid}'
        return cadena

""" @app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/thank_you')
def thank_you():
    first = request.args.get('first') 
    last = request.args.get('last') 
    return render_template('thank_you.html', first=first, last=last)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
 """