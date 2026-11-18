
# usando so o while 

resposta = 'S'
contador = 1 
soma = 0

while resposta = 'S':
    print(contador)
    despeza = float(input('informe a despeza: '))
    soma = soma + despeza

    contador += 1
    print(f'total: {soma}')

    resposta = input('\nquer continuar? [S/N]').upper()

    while resposta != 'S' and resposta != 'N':
        resposta = input('Resposta inválida! Digite S ou N: ').upper()

    if resposta == 'N':
        break
