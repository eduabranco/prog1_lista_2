TIPO=str(input("TIPO DE CARNE (FILE DUPLO / ALCATRA / PICANHA)\n")).upper()
KG=float(input("\nQuantos Quilos?\n"))
if TIPO=="FILE DUPLO":
    if KG<=5:
        price=KG*4.9
    elif KG>5 and KG>0:
        price=KG*5.8
    else: print("Valor inválido.")
elif TIPO=="ALCATRA":
    if KG<=5:
        price=KG*5.9
    elif KG>5 and KG>0:
        price=KG*6.8
    else: print("Valor inválido.")
elif TIPO=="PICANHA":
    if KG<=5:
        price=KG*6.9
    elif KG>5 and KG>0:
        price=KG*7.8
    else: print("Valor inválido.")
else: 
    print("Tipo inválido.")
    exit()

PAG=str(input("Deseja pagar com o cartão Tabajara?(s/n)\n")).upper()
if PAG=="S":desc=price*0.05
else: desc=0

print(f"\nTipo de carne: {TIPO}")
print(f"Preço Total: R${price:.2f}")
print(f"Pagamento com cartão:{PAG}")
print(f"Desconto: R${desc:.2f}")
print(f"Valor a pagar: R${(price-desc):.2f}")