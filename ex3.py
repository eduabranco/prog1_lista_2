usuario = int(input('Digite um número: '))
if usuario == 1:
    dia = 'Domingo'
elif usuario == 2:
    dia = 'Segunda-feira'
elif usuario == 3:
    dia = 'Terça-feira'
elif usuario == 4:
    dia = 'Quarta-feira'
elif usuario == 5:
    dia = 'Quinta-feira'
elif usuario == 6:
    dia = 'Sexta-feira'
elif usuario == 7:
    dia = 'Sabado'
else:
    print(f'Número inválido.') 
    exit()
print(f'O número digitado equivale a um(a) {dia}.')