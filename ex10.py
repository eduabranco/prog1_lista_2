n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
n3 = float(input('Digite a terceira nota do aluno: '))

media = (n1+n2+n3)/3

if media < 7:
    print(f'O aluno alcançou a média: {media} \nREPROVADO!')
elif media >= 7 and media < 10:
    print(f'O aluno alcançou a média: {media} \nAPROVADO!')
elif media == 10:
    print(f'O aluno alcançou a média: {media} \nAPROVADO COM DISTINÇÃO!')
else:
    print('Média inválida.')

