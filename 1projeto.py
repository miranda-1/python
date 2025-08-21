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

def voltar_ao_menu():
    input('\nDigite uma tecla para voltar ao menu inicial: ')
    main()

def opcao_invalida():
    print('Opção Inválida!\n')
    voltar_ao_menu()

def exibir_subtitulos(texto):
    os.system('cls')
    print(texto)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulos('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'\nO restaurante {nome_do_restaurante} foi cadastrado com sucesso!!!\n')
    voltar_ao_menu()
    
def listar_restaurantes():
    exibir_subtitulos('Listando os restaurantes:')
    for restaurante in restaurantes:
        print(f'.{restaurante}')
    voltar_ao_menu()

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
