a = float(input('Digite o valor de "A": '))
b = float(input('Digite o valor de "B": '))
c = float(input('Digite o valor de "C": '))

if a != 0:
    delta = b**2-(4*a*c)
    x1 = (-(b)+(delta**(1/2)))/(2*a)
    x2 = (-(b)-(delta**(1/2)))/(2*a)
    if delta > 0:
        print(f'As raízes da equação são: {x1} e {x2}')
    elif delta == 0:
        print(f'Delta é igual a zero, equação possui apenas uma raíz: {x1}')
    else:
        print(f'Delta é negativo (Delta = {delta}), a equação não possui raízes reais.')
else:
    print('"A" não pode ser zero (0), não é uma equação do segundo grau.')