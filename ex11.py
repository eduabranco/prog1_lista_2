nota100=nota50 = nota20 = nota10 = nota5 = nota1 = 0
usuario = float(input('Qual valor você deseja sacar: R$'))
if usuario>600 or usuario<10:
    print("Este valor não pode ser sacado.")
    exit()
print(' ')
if usuario >= 100:
    nota100 = usuario // 100
    usuario = usuario - (nota100*100)
if usuario >= 50:
    nota50 = usuario // 50
    usuario = usuario - (nota50*50)
if usuario >= 10:
    nota10 = usuario // 10
    usuario = usuario - (nota10*10)
if usuario >= 5:
    nota5 = usuario // 5
    usuario = usuario - (nota5*5)
if usuario >= 1:
    nota1 = usuario // 1
    usuario = usuario - (nota1*1)
if nota100 != 0:
    print(f'Total de {nota100:.0f} nota(s) de R$100,00')
if nota50 != 0:
    print(f'Total de {nota50:.0f} nota(s) de R$50,00')
if nota10 != 0:
    print(f'Total de {nota10:.0f} nota(s) de R$10,00')
if nota5 != 0:
    print(f'Total de {nota5:.0f} nota(s) de R$5,00')
if nota1 !=0:
    print(f'Total de {nota1:.0f} nota(s) de R$1,00')