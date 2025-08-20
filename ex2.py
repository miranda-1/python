try:
    numero = int(input('Digite o numero: '))

    if numero % 2 == 0:
        print('O numero eh par')

    else:
        print('O numero eh impar')

except ValueError:
    print('Digite apenas numeros')