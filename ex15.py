contador = 0
print('Digite "s" para sim e "n" para não')

q1 = str(input('\nTelefonou para a vitíma ? [s/n] ')).upper()
if q1 == 'S':contador += 1

q2 = str(input('Esteve no local do crime ? [s/n] ')).upper()
if q2 == 'S':contador += 1

q3 = str(input('Mora perto da vítim a ? [s/n] ')).upper()
if q3 == 'S':contador += 1

q4 = str(input('Devia para a vítima ? [s/n] ')).upper()
if q4 == 'S':contador += 1

q5 = str(input('Já trabalhou com a vítima ? [s/n] ')).upper()
if q5 == 'S': contador += 1

if contador == 2:print('O individuo é suspeito.')
elif contador <= 4:print('O individuo é cumplice.')
elif contador == 5:print('O individuo é o assassino.')
else:print('O individuo é inocente.')
