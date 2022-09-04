n1 = float(input('Qual foi a primeira nota do aluno: '))
n2 = float(input('Qual foi a segunda nota do aluno: '))

media = (n1 + n2)/2
if media <= 10:
    if media < 4:
        conceito = 'E'
    elif media < 6:
        conceito = 'D'
    elif media < 7.5:
        conceito = 'C'
    elif media < 9:
        conceito = 'B'
    elif media <= 10:
        conceito = 'A'
    if media >= 6:
        situacao = 'APROVADO'
    else:
        situacao = 'REPROVADO'
    print(f'-- A primeira nota foi {n1} e a segunda nota foi {n2} \n-- Média do aluno: {media} \n-- Conceito: {conceito} \n-- Situação do aluno: {situacao}')
else:
    print(f'Média inválida.')
    
