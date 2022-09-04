ano = int ( input( 'Forneca um ano: '))
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print ('O ano fornecido é bissexto.')
else:
    print ('O ano fornecido não e bissexto')