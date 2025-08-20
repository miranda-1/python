
usuario = input('Digite seu nome de usuario:\n')

senha = input('Digite sua senha:\n')

print('CADASTRADO!')

while True:
    usuario1 = input('Digite seu usuario:\n')

    senha1 = input('Digite sua senha:\n')

    if usuario1 == usuario and senha1 == senha:
        print('ENTROU NO SISTEMA!')
        break
    else:
        print('usuario ou senha incorretos!\nTente novamente!')
