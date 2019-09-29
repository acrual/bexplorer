import bitcoin
from bitcoin.rpc import RawProxy

p = RawProxy()
info = p.getblockchaininfo()

class Tx(object):
    def __init__(self, txid):
        self.txid = txid
        self.raw = p.getrawtransaction(self.txid)
        self.tx = p.decoderawtransaction(self.raw)

    def __str__(self):
        cadena = "txid: " + self.txid + "\n"
        if not self.esCoinbase():
            for i in range(len(self.obtenerVins()[0])):
                # print("aquí: ", str(self.obtenerVins()))
                tx_input = Tx(str(self.obtenerVins()[0][i]))
                cadena += "txid de input: " + str(tx_input.txid) + "\n"
                cadena += " desde " + str(tx_input.txid) + " y " + "n " + str(self.obtenerVins()[1][i]) + " salen " + str(tx_input.tx['vout'][self.obtenerVins()[1][i]]['value']) + "\n"
        else:
            cadena += "es coinbase" + "\n"
        
        for i in range(len(self.obtenerVouts()[0])):
            cadena += "en " + str(self.obtenerVouts()[0][i]) + " entran " + str(self.obtenerVouts()[1][i]) + "\n"
        return cadena


    def esNullType(self, i):
        if self.tx['vout'][i]['scriptPubKey']['type'] == 'nulldata':
            return True
        else:
            return False

    def esCoinbase(self):
        if 'coinbase' in list(self.tx['vin'][0]):
            return True
        else:
            return False

    def obtenerVins(self):
        listains = []
        ncadains = []
        for i in range(len(self.tx['vin'])):
            listains.append(self.tx['vin'][i]['txid'])
            ncadains.append(self.tx['vin'][i]['vout'])
        return listains, ncadains

    def obtenerVouts(self):
        cantidades = []
        direcciones = []
        for i in range(len(self.tx['vout'])):
            if not self.esNullType(i):
                # print("probando", self.tx['vout'][i]['scriptPubKey']['addresses'][0])
                cantidades.append(str(self.tx['vout'][i]['value']))
                direcciones.append(str(self.tx['vout'][i]['scriptPubKey']['addresses'][0]))
        return direcciones, cantidades
        
            

    # hay que 