salario = float(input('Digite o salario do colaborador: '))
if salario <= 280:
    valor_percent = '20%'
    percentual = ((20/100)*salario)
    aumento = salario + percentual
elif salario <= 700:
    valor_percent = '15%'
    percentual = ((15/100)*salario)
    aumento = salario + percentual
elif salario <= 1500:
    valor_percent = '10%'
    percentual = ((10/100)*salario)
    aumento = salario + percentual
elif salario > 1500:
    valor_percent = '5%'
    percentual = ((5/100)*salario)
    aumento = salario + percentual
print(f'\nVocê recebia um salário de R${salario}.')
print(f'O aumento percentual aplicado será de {valor_percent}.')
print(f'O valor do aumento será de R${percentual}.')
print(f'O novo salário, após o aumento, será de R${aumento}.')