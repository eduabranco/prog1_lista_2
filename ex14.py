num1=float(input("Digite um primeiro valor numérico: "))
num2=float(input("Digite um segundo valor numérico: "))
calc=input("Escolha a operação (+, -, *, /, Qualquer outro: Encerra o programa)\n")

if calc=="+":
    rsp=num1+num2
elif calc=="-":
    rsp=num1-num2
elif calc=="*":
    rsp=num1*num2
elif calc=="/":
    rsp=num1/num2
else:exit()

if abs(rsp)%2==0:pi="par"
else:pi="ímpar"

if rsp>0:pn="positivo"
else:pn="negativo"

if rsp-int(rsp)==0:fi="inteiro."
else:fi="decimal"

if rsp==0:print("Este número é 0")
else:print(f"O resultado é {rsp}, um número {pi}, {pn}, {fi}")