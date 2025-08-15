print('🅙🅐🅟🅐 🅔🅧🅟🅡🅔🅢🅢\n')

print('1-Cadastrar restaurante')
print('2-Listar restaurante ')
print('3-Ativar restaurante')
print('4-Sair\n')

opcao_escolhida = int(input('Escolha uma opção: '))
# opcao_escolhida = int(opcao_escolhida)

if opcao_escolhida == 1:
    print('Cadastrar Restaurante')
elif opcao_escolhida == 2:
    print('Listar Restaurantes')
elif opcao_escolhida == 3:
    print('Ativar restaurante')
else:
    print('Encerrando o programa')
