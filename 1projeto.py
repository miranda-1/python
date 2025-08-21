import os

restaurantes = ['Japa Lounge', 'Burguer King']

def exibir_o_nome():
    print('===== JAPA EXPRESS =====\n')


def exibir_as_opcoes():
    print('1 - Cadastrar restaurante')
    print('2 - Listar restaurante ')
    print('3 - Ativar restaurante')
    print('4 - Sair\n')

def finalizando_app():
    os.system('cls')
    print('Finalizando o app')

def opcao_invalida():
    print('Opção Inválida!\n')
    input('Digite uma tecla para voltar ao menu inicial!')
    main()

def cadastrar_novo_restaurante():
    os.system('cls')
    print('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!!!\n')
    input('Digite uma tecla para voltar ao menu principal:')
    main()
    
def listar_restaurantes():
    os.system('cls')
    print('Listando os restaurantes:')

    for restaurante in restaurantes:
        print(f'.{restaurante}')

    input('Digite uma tecla para voltar ao menu principal:')
    main()

def escolher_as_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
        elif opcao_escolhida == 4:
            finalizando_app()
        else:
            opcao_invalida()
    except ValueError:
        print("Digite apenas números válidos!\n")
        escolher_as_opcoes()

def main():
    os.system('cls')
    exibir_o_nome()
    exibir_as_opcoes()
    escolher_as_opcoes()

if __name__ == '__main__':
    main()
