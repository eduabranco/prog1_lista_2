valor_hora = float(input('Qual o valor da sua hora trabalhada: '))
hora_trabalhada = float(input('Quantas horas você trabalho no mês: '))
salario_bruto = valor_hora*hora_trabalhada

if salario_bruto < 900:
    percent = '0%'
    ir = 0
elif salario_bruto <= 1500:
    percent = '5%'
    ir = (5/100)*salario_bruto
elif salario_bruto <= 2500:
    percent = '10%'
    ir = (10/100)*salario_bruto
elif salario_bruto > 2500: 
    percent = '20%'
    ir = (20/100)*salario_bruto
FGTS = (11/100)*salario_bruto
INSS = (10/100)*salario_bruto
salario_liquido = salario_bruto - ir - INSS
print(f'-- Salário Bruto: ({hora_trabalhada}*{valor_hora}): R$  {salario_bruto}')
print(f'-- (-) IR ({percent}): R$   {ir}')
print(f'-- (-) INSS ( 10%): R$  {INSS}')
print(f'-- FGTS (11%): R$  {FGTS}')
print(f'-- Total de descontos: R$  {ir + INSS}')
print(f'-- Salário Liquido: R$  {salario_liquido}')