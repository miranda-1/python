import os


def escolheu_numeros():
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    for numero in numeros:
        print(f'.{numero}')

def escolheu_listas():
    listas = ['joao', 'pedro', 'hugo', 'victor']
    for lista in listas:
        print(f'.{lista}')

def data_nascimento():
    nascimentos = ['nasci em 2003', 'estamos em 2025']
    for nascimento in nascimentos:
        print(f'.{nascimento}')

def encerrando():
    os.system('cls')
    print('encerrando o programa')

def voltando_menu():
    print('Opcao invalida!!')
    input('\nDigite uma tecla para voltar ao menu: ')
    main()

def lista_encontrada():
    print('\n Aqui esta a lista pedida')
    input('Digite uma tecla para voltar ao menu: ')
    main()

def exibir_as_opcoes():
    print('Digite qual lista deseja')
    print('1.lista de numeros')
    print('2.lista de nomes')
    print('3.lista do aniversario')
    print('0.encerrando')

def escolha_as_opcoes():
    escolha = int(input('Digite qual sua lista: '))

    if escolha == 1:
        escolheu_numeros()
        
        lista_encontrada()
    elif escolha == 2:
        escolheu_listas()
        
        lista_encontrada()
    elif escolha == 3:
        data_nascimento()
        
        lista_encontrada()
    elif escolha == 0:
        encerrando()
    else:
        voltando_menu()
        

def main():
    os.system('cls')
    exibir_as_opcoes()
    escolha_as_opcoes()


if __name__ == '__main__':
    main()
