# linea 19 de transaction, está obteniendo el txid y n del que sale el bitcoin pero lo que tiene que obtener
# es el address. Corregir. A continuación:
# # lo que falta es coger cada dirección de entrada y salida e ir aplicándole lo que cambia el saldo
# e ir grabándola en la bbdd. Si unanueva dirección está en la bbdd, debe actualizarse el saldo
# si no está, se graba con el movimiento de esa nueva tx

from transaction import Tx
import bitcoin
from bitcoin.rpc import RawProxy
from bitcoin import SelectParams
SelectParams('testnet')

def obtenerTransacciones(bloque):
    txids = []
    info = p.getblockhash(bloque)
    bloque_explorado = p.getblock(info)
    for txid in bloque_explorado['tx']:
        tx = Tx(txid)
        print(tx.__str__())
    

def imprimirTransacciones(bloque_origen, bloque_final):
    transacciones = []
    for i in range(bloque_origen, bloque_final):
        transacciones = obtenerTransacciones(i)
    # loop de las transacciones de cada bloque debería grabarse en la bbdd aquí (tabla de tx)
    for txid in transacciones:
        tx = Tx(txid)
        print(tx.__str__())

p = RawProxy()
info = p.getblockchaininfo()
hasta_que_bloque = info['blocks']
""" bloque_origen = int(input("Dime DESDE que bloque: "))
bloque_final = int(input("Dime HASTA que bloque: ")) """
bloque_origen = 1579713
bloque_final = 1579714
obtenerTransacciones(bloque_origen)



