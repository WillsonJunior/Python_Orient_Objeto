class Conta:
  def __init__(self, numero, titular, saldo, limite):
    self.__numero= numero
    self.__titular= titular
    self.__saldo= saldo
    self.__limite= limite

  def extrato(self):
    print("saldo de {} do titular {}".format(self.saldo, self.titular))
  
  def deposita(self,valor):
    self.saldo += valor
  def saca(self,valor):
    self.saldo -= valor
def trans(self, valor, origem, destino):
  origem.sacar(valor)
  destino.deposita(valor)
