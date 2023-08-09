from sistema import sistema

class sistema_cliente:
    
    def __init__(self) -> None:
        pass

    def operar_sistema(self):
        sis = sistema()
        li = [s for s in sis.df['CPF']]
        print(f'\nSeja bem-vindo(a) {sis.df.loc[li.index(sis.cpf), "Nome"]}!\n')
        while True:
            cond = input(sis.df_menu.loc[0,'menu'])
            if cond == '1':
                sis.depositar()
            elif cond == '2':
                sis.sacar()
            elif cond == '3':
                sis.mostrar_extrato()
            elif cond == '4':
                sis.cpf = input('Digite o CPF: ')
            elif cond == '5':
                sis.criar_conta()
                li = [s for s in sis.df['CPF']]
                print(f'\nSeja bem-vindo(a) {sis.df.loc[li.index(sis.cpf), "Nome"]}!\n')
            elif cond == '6':
                break
            elif cond == '7':
                print(sis.df)
            sis.atualizar()
            
            
banco = sistema_cliente()
banco.operar_sistema()