import datetime
class banco:

    def __init__(self,extrato = '\n', saldo = 0) -> None:
        self.extrato = extrato
        self.saldo   = saldo
        self.limite_saque = 0
        self.CONSTANTE = {'menu':'\n[1] Depositar\n[2] Sacar\n[3] Extrato\n[4] Sair\n\n',
                          'limite' : 500,
                          'limite_saques' : 3,
                          'data' : datetime.datetime.today().date()}

    def depositar(self,n):
        if n == 1:
            valor = float(input('\nInforme o valor do depósito: '))
            if valor > 0:
                self.saldo += valor
                self.extrato += f'Depósito: R$ {valor:.2f} as {datetime.datetime.today()}\n'
            else:
                print('Valor inválido!')
    
    def sacar(self, n):
        if n == 2:
            if datetime.datetime.today().date() == self.CONSTANTE['data'] and self.limite_saque < 3:
                valor = float(input('\nDigite o valor de saque: '))
                if valor <= self.CONSTANTE['limite'] and valor <= self.saldo and valor > 0:
                    self.saldo -= valor
                    self.extrato += f'Saque: R$ {valor:.2f} as {datetime.datetime.today()}\n'
                    self.limite_saque += 1
                else:
                    print('\nValor inválido!\n')
            else:
                print('\nLimite de saques diarios atingido!\n')
 
    def mostrar_extrato(self, n):
        if n == 3:
            print(self.extrato)
            print(f'Saldo: R$ {self.saldo:.2f}\n')

cliente = banco()
while True:
    try:
        cond = int(input(cliente.CONSTANTE['menu']))
    except ValueError:
        print('\nDigite apenas numeros inteiros\n')
        continue
    if cond == 4:
        break
    if cond not in [1,2,3,4]:
        print('\nvalor invalido\n')
        continue
    cliente.depositar(cond)
    cliente.sacar(cond)
    cliente.mostrar_extrato(cond)