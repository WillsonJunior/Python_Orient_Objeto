#importando a classe

from conta import Conta

#criando 3 contas

conta = Conta(123456, "junior", 90.0 , 1000.0)

conta1 = Conta(789456, "Pietro", 90.0 , 1000.0)

conta2 = Conta(57823, "maria lucia", 90.0 , 1000.0)

#testando o mtodo de tranferência
#conta1.transfere(10, conta2)
#conta1.extrato()
#conta2.extrato()

#testando os metodos criado get e set

conta.get_saldo()
