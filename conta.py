class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        

    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo,self.__titular))

    def deposita(self, valor):
        self.__saldo += valor
    
    def __pode_sacar(self,valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <=valor_disponivel_a_sacar
    
    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("voce não tem limite suficiente, o valor[] não foi aprovado".format(valor))
        
#metodo de tranferencia entre contas
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
#metodo de para retornar saldo,limite e titular    
    
    def get_saldo(self):
        return self.__saldo
    def get_titular(self):
        return self.__titular
    @property
    def limite(self):
        return self.__limite
    
#funções para modificar limiti
    @limite.setter
    def limite(self, limite):
        self.__limite= limite
        
    @staticmethod
    def codigos_bancos():
        return {"BB":"001", "CAIXA":"104", "Bradesco":"237"}




