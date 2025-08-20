import os
def exibir_o_nome(): 
    print('🅙🅐🅟🅐 🅔🅧🅟🅡🅔🅢🅢\n')

def exibir_as_opcoes():
    print('1-Cadastrar restaurante')
    print('2-Listar restaurante ')
    print('3-Ativar restaurante')
    print('4-Sair\n')

def finalizando_app():
    os.system('cls')

    print('Finalizando o app')

def escolher_as_opcoes():
    opcao_escolhida = int(input('Escolha uma opção: '))

    if opcao_escolhida == 1:
        print('Cadastrar Restaurante')
    elif opcao_escolhida == 2:
        print('Listar Restaurantes')
    elif opcao_escolhida == 3:
        print('Ativar restaurante')
    else:
        finalizando_app()

def main():
    exibir_o_nome()
    exibir_as_opcoes()
    escolher_as_opcoes()

if __name__ == '__main__':
    main()