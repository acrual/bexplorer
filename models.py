import os
from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)

""" user = os.environ['POSTGRES_USER ']
pw = os.environ['POSTGRES_PW ']
url = os.environ['POSTGRES_URL ']
db = os.environ['POSTGRES_DB '] """
user = 'postgres'
pw = 'postgres'
pw2 = 'aePOnw8;0c73)LTb'
url ='127.0.0.1:5433'
db = 'BitcoinExplorer'
print(user, pw, url, db)
connect = 'postgresql://{}:{}@{}/{}'.format(user, pw, url, db) # +psycopg2 AND .format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
print("connect es", connect)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{}:{}@{}/{}'.format(user, pw, url, db)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning

db = SQLAlchemy(app)

Migrate(app, db)
# ****************************************
class Balances(db.Model):
    __tablename__ = 'balances'
    id = db.Column(db.Integer, primary_key = True)
    address = db.Column(db.Text)
    balance = db.Column(db.Float)
    block = db.Column(db.Integer)
    txid = db.Column(db.Text)

    def __init__(self, address, amount, input, block, txid, balance=0):
        self.address = address
        self.amount = amount
        self.input= input
        self.balance = balance
        if self.input and self.balance > 0:
            self.balance = self.balance - self.amount
        else:
            self.balance = self.balance + self.amount
        self.block = block
        self.txid = txid

    def __repr__(self):
        cadena = f'Address {self.address} has a balance of {self.balance} \n'
        cadena += f'Last Block is {self.block} and last transaction is {self.txid}'
        return cadena

class Transactions(db.Model):
    __tablename__ = 'transactions'
    id = db.Column(db.Integer, primary_key = True)
    txid = db.Column(db.Text)
    input = db.Column(db.Text)
    txidIn = db.Column(db.Text)
    txidOut = db.Column(db.Text)
    amount = db.Column(db.Float)

    def __init__(self, txid, input, txidIn, txidOut, amount, fees):
        self.txid = txid
        self.input = input
        self.txidIn= txidIn
        self.txidOut = txidOut
        self.amount = amount
        self.fees = fees

    def __repr__(self):
        fees = 0.0
        cadena = "txid: " + self.txid + "\n"
        if not self.esCoinbase():
            for i in range(len(self.obtenerVins()[0])):
                tx_input = Tx(str(self.obtenerVins()[0][i]))
                cadena += "txid input: " + str(tx_input.txid) + "\n"
                cadena += "desde dire " + str(tx_input.obtenerVoutsN(self.obtenerVins()[1][i])[0]) + " salen " + str(tx_input.tx['vout'][self.obtenerVins()[1][i]]['value']) + "\n"
                if not tx_input.esNullType(self.tx['vin'][i]['vout']):
                    fees += float(tx_input.tx['vout'][self.obtenerVins()[1][i]]['value'])
        else:
            cadena += "es coinbase" + "\n"
        for i in range(len(self.obtenerVouts()[0])):
            cadena += "en " + str(self.obtenerVouts()[0][i]) + " entran " + str(self.obtenerVouts()[1][i]) + "\n"
            if not self.esCoinbase():
                fees -= float(self.obtenerVouts()[1][i])
        return cadena + "\n" + "fees: " + str(fees) + "\n"

class TransactionLists(db.Model):
    __tablename__ = 'lists'
    id = db.Column(db.Integer, primary_key = True)
    txidList = db.Column(db.Text)

    def __init__(self, txid=[]):
        self.txid = txid
        self.input = input
        self.txidIn= txidIn
        self.txidOut = txidOut
        self.amount = amount
        self.fees = fees

    def __repr__(self):
        for i in range(len(self.txid)):
            cadena = self.txid[i]
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