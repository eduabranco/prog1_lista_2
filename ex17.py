valor_maca = float(input('Quantos kilos de maçã você quer comprar: Kg '))
valor_morango = float(input('Quantos kilos de morango você quer comprar: Kg '))
if valor_maca <= 5:
    maca = 1.8*valor_maca
else:
    maca = 1.5*valor_maca
if valor_morango <= 5: 
    morango = 2.5*valor_morango
else:
    morango = 2.2*valor_morango
total = morango + maca
valor_cliente = valor_maca+valor_morango
if valor_cliente > 8 or total > 25:
    total = total-((10/100)*total)

print(f'O cliente irá pagar R${total}')