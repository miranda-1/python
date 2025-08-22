import os

restaurantes = [{'Nome':'Japa lounge', 'Categoria': 'Japonesa', 'ativo':False},
                {'Nome':'Pizza hut', 'Categoria': 'Pizza', 'ativo':True},
                {'Nome':'Burguer King', 'Categoria': 'Lanche', 'ativo':False}]

def exibir_o_nome():
    print('===== JAPA EXPRESS =====\n')

def exibir_as_opcoes():
    print('1 - Cadastrar restaurante')
    print('2 - Listar restaurante ')
    print('3 - Alternar estado do restaurante')
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
    linha = '*' * (len(texto) )
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulos('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do {nome_do_restaurante}: ')
    dados_do_restaurante = {'Nome':nome_do_restaurante, 'Categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'\nO restaurante {nome_do_restaurante} foi cadastrado com sucesso!!!\n')
    voltar_ao_menu()
    
def listar_restaurantes():
    exibir_subtitulos('Listando os restaurantes:')
    
    print(f'|{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Status'} \n')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['Nome']
        categoria = restaurante['Categoria']
        validacao = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'|{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {validacao}|')
    voltar_ao_menu()

def alternando_ativacao():
    exibir_subtitulos('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado de ativaçao: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['Nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante ['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado!')

    voltar_ao_menu()

def escolher_as_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternando_ativacao()
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
