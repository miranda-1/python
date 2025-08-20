ponto_x = int(input('Digite a coordenada x:\n'))
ponto_y = int(input('Digite a coordenada y:\n'))

if ponto_x > 0 and ponto_y > 0:
    print('Voce se encontra no primeiro quadrante!')
elif ponto_x < 0 and ponto_y > 0:
    print('Voce se encontra no segundo quadrante!')
elif ponto_x < 0 and ponto_y < 0:
    print('Voce se encontra no terceiro quadrante!')
elif ponto_x > 0 and ponto_y < 0:
    print('Voce se encontra no quarto quadrante!')
else:
    print('O eixo esta localizado no eixo ou origem!')


