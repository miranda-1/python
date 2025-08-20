try:

    idade = int(input('Qual sua idade? '))

    if idade <= 12:
        print('Você está na categoria criança.')

    elif 13 <= idade <= 18:
        print('Você está na categoria adolescente.')

    else:
        print('Você está na categoria adulto.')

except ValueError:
    print('Digite apenas numeros, por favor!')