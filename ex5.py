lado1 = float(input('Qual o tamanho do primeiro lado: '))
lado2 = float(input('Qual o tamanho do segundo lado: '))
lado3 = float(input('Qual o tamanho do terceiro lado: '))

if lado1+lado2 >= lado3 and lado3+lado2 >= lado1 and lado3+lado1 >= lado2:
    if lado1 == lado2 == lado3:
        print(f'Os valores mencionados formam um triângulo equilátero.')
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print(f'Os valores mencionados formam um triângulo isósceles.')
    else:
        print(f'Os valores mencionados formam um triângulo escaleno.')
else:
    print(f'Os valores mencionados não formam um triângulo')
        