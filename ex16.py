c=str(input("Escolha um combustível(A/G)\n")).upper()
l=float(input("\nQuantos litros?\n"))
if c=="A":
    price=l*1.9
    if l>20:price-=price*.05
    elif l<=20 and l>0: price-=price*.03
    else:
        print("Valor inválido.")
        exit()
elif c=="G":
    price=l*2.5
    if l>20:price-=price*.06
    elif l<=20 and l>0: price-=price*.04
    else:
        print("Valor inválido.")
        exit()
else:
    print("Tipo inválido.")
    exit()
print(f"Valor a ser pago: R${price:.2f}")