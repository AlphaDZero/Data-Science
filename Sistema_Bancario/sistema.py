import pandas as pd
import datetime

class sistema:

    def __init__(self,*,cpf = input('Digite o CPF: ')) -> None:
        self.cpf = cpf
        self.df = pd.read_csv('Sistema_Bancario/Dados/data.csv')
        self.df_menu = pd.read_csv('Sistema_Bancario/Dados/menu.csv')
        self.df_menu = self.df_menu.drop('Unnamed: 0', axis=1)
        self.df = self.df.drop('Unnamed: 0', axis=1)
        self.df['CPF'] = [str(int(s)) for s in self.df['CPF']]
        self.df['Limite_diario'] = [int(s) for s in self.df['Limite_diario']]
        self.df['Saldo'] = [float(s) for s in self.df['Saldo']]
        li = [s for s in self.df['CPF']]
        if self.cpf not in li:
            self.criar_conta()
            self.atualizar()
    
    def atualizar(self):
        self.df.to_csv('Sistema_Bancario/Dados/data.csv')
    
    def depositar(self):
        while True:
            try:
                valor = float(input('\nInforme o valor do depósito: '))
                if valor > 0:
                    li = [s for s in self.df['CPF']]
                    self.df.loc[li.index(self.cpf), 'Saldo'] += valor
                    self.df.loc[li.index(self.cpf), 'Extrato'] += f'Depósito: R$ {valor:.2f} as {datetime.datetime.today()}\n'
                    break
                else:
                    print('Valor inválido!')
            except ValueError:
                print('Valor inválido!')
    
    def criar_conta(self):
        while True:
            self.cpf = input('Digite o CPF: ')
            if self.cpf in self.df['CPF']:
                print('Ja existe esse CPF!')
                continue
            break
        self.df.loc[len(self.df['CPF']), 'CPF'] = self.cpf
        li = [s for s in self.df['CPF']]
        self.df.loc[li.index(self.cpf),'Nome'] = input('Digite seu nome: ')
        self.df.loc[li.index(self.cpf), 'Local'] = input('Digite seu local: ')
        self.df.loc[li.index(self.cpf), 'Data'] = datetime.datetime.today().date()
        self.df.loc[li.index(self.cpf), 'Limite_diario'] = 0
        self.df.loc[li.index(self.cpf), 'Extrato'] = '\n'
        self.df.loc[li.index(self.cpf), 'Saldo'] = 0

    def mostrar_extrato(self):
        li = [s for s in self.df['CPF']]
        print(f'Usuario: {self.df.loc[li.index(self.cpf), "Nome"]}\n')
        print(self.df.loc[li.index(self.cpf), 'Extrato'])
        print(f'Saldo: R$ {self.df.loc[li.index(self.cpf), "Saldo"]:.2f}\n')

    def sacar(self):
        while True:
            li = [s for s in self.df['CPF']]
            data = datetime.datetime.today().date()
            limite = self.df.loc[li.index(self.cpf),'Limite_diario']
            data_sistema = self.df_menu.loc[0,'data']
            data_user = self.df.loc[li.index(self.cpf),'Data']
            if data != data_sistema:
                self.df_menu.loc[0,'data'] = datetime.datetime.today().date()
                self.df_menu.to_csv('Sistema_Bancario/Dados/menu.csv')
                continue
            if data != data_user:
                self.df.loc[li.index(self.cpf),'Data'] = data
                self.df.loc[li.index(self.cpf),'Limite_diario'] = 0
                continue
            if data == data_user and limite < 3:
                valor = float(input('\nDigite o valor de saque: '))
                if valor <= 500 and valor <= self.df.loc[li.index(self.cpf),'Saldo'] and valor > 0:
                    self.df.loc[li.index(self.cpf),'Saldo'] -= valor
                    self.df.loc[li.index(self.cpf),'Extrato'] += f'Saque: R$ {valor:.2f} as {datetime.datetime.today()}\n'
                    self.df.loc[li.index(self.cpf),'Limite_diario'] += 1
                    break
                else:
                     print('\nValor inválido!\n')
                     continue
            else:
                print('\nLimite de saques diarios atingido!\n')
                break
