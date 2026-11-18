meta = 2000.00
operacao = 'S'
while operacao == 'S':
    venda = float(input('\nqual o valor das suas vendas: '))
    atingimento = (venda / meta) * 100
    print(f'suas vendas foram de: {venda}')
    print(f'Seu porcentual foi: {atingimento}%')

    operacao = input('\ndeseja continuar: [S/N]').upper()





