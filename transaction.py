from bitcoin.rpc import RawProxy

p = RawProxy()
info = p.getblockchaininfo()

class Tx(object):
    def __init__(self, txid):
        self.txid = txid
        self.raw = p.getrawtransaction(self.txid)
        self.tx = p.decoderawtransaction(self.raw)

    def __str__(self):
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
# ahora hay que hacer esta función de abajo que debería devolver 
    def txabd(self):
        fees = 0.0
        diresin = []
        diresout = []
        amountsout = []
        amountsin = []
        txinputs = []
        if not self.esCoinbase():
            for i in range(len(self.obtenerVins()[0])):
                tx_input = Tx(str(self.obtenerVins()[0][i]))
                txinputs.append(self.obtenerVins([0][i]))
                diresin.append(tx_input.obtenerVoutsN(self.obtenerVins()[1][i])[0])
                amountsin.append(tx_input.tx['vout'][self.obtenerVins()[1][i]]['value'])
                if not tx_input.esNullType(self.tx['vin'][i]['vout']):
                    fees += float(tx_input.tx['vout'][self.obtenerVins()[1][i]]['value'])
        else:
            cadena = "es coinbase" + "\n"
        for i in range(len(self.obtenerVouts()[0])):
            diresout.append(self.obtenerVouts()[0][i])
            amountsout.append(self.obtenerVouts()[1][i])
            if not self.esCoinbase():
                fees -= float(self.obtenerVouts()[1][i])
        return txinputs, diresin, amountsin, diresout, amountsout, fees


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
        
    def obtenerVoutsN(self, n):
        cantidad = self.tx['vout'][n]['value']
        dire = self.tx['vout'][n]['scriptPubKey']['addresses'][0]
        return dire, cantidad
