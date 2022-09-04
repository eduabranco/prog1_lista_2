numero = abs(int(input('Digite um número: ')))
centena = dezena = unidade = 0

if numero>=1000:
    print("Número inválido.")
    exit()
    
if numero >= 100:
    centena = numero//100

if numero >= 10 and centena % 100 != 0 or centena == 0:
    dezena = (numero-(centena*100))//10

if numero >= 1 and dezena % 10 != 0 or dezena == 0:
    unidade = ((numero-(centena*100))-(dezena*10))

print(f'O número possui {centena} centena(s), {dezena} dezena(s) e {unidade} unidade(s)')
    