dia = int(input('Qual dia você nasceu:'))
mes = int(input('Qual mês você nasceu: '))
ano = int(input('Qual ano você nasceu:'))

if dia < 0 or dia > 31:
    print('O dia digitado é inválido.')
elif mes < 0 or mes > 12:
    print('O mês digitado é inválido.')
elif ano < 1000 or ano > 2022:
    print('O ano digitado é inválido.')
else:
    print(f'Sua data de nacimento é: {dia}/{mes}/{ano}')

