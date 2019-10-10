from transaction import Tx
from bitcoin.rpc import RawProxy
import models
from models import db, Balances, Transactions, TransactionLists


## CREATE
# (address, amount, input, block, txid, balance=0)
registro1 = Balances('dire', 5.0, True, 70000, 'transaction1')
db.session.add(registro1)
db.session.commit()

## READ
all_puppies = Balances.query.all()
print(all_puppies)

def direEnBbdd(dire):
    dires = Balances.query.filter_by(address = dire)
    if dire in dires.all():
        return True
    else:
        return False

def obtenerTransacciones(bloque):
    info = p.getblockhash(bloque)
    bloque_explorado = p.getblock(info)
    for txid in bloque_explorado['tx']:
        tx = Tx(txid)
        for i in range(len(tx.txabd[1])):
            if not direEnBbdd(tx.txabd[1][i]):
                registro = Balances(tx.txabd[1][i], tx.txabd[2][i], True, bloque, tx.txabd[0])
            else:
                dires = Balances.query.filter_by(address = tx.txabd[1][i])
                dires.balance = dires.balance - tx.amount
                dires.block = bloque
                dires.txid = txid
        for i in range(len(tx.txabd[3])):
            if not direEnBbdd(tx.txabd[1][i]):
                registro = Balances(tx.txabd[3][i], tx.txabd[4][i], False, bloque, tx.txabd[0])
            else:
                dires = Balances.query.filter_by(address = tx.txabd[3][i])
                dires.balance = dires.balance + tx.amount
                dires.block = bloque
                dires.txid = txid
        db.session.add(registro)
        db.session.commit()




p = RawProxy()
info = p.getblockchaininfo()
hasta_que_bloque = info['blocks']
bloque_origen = 1580000
bloque_final = 1580001
obtenerTransacciones(bloque_origen)
if bbdd_vacia:
    db.create_all()
meterDatos()



