print('dite o seu sexo')

resposta = ''

while not (resposta == 'F' or resposta == 'M'):

    print(' \n[F] feminino\n[M] masculino\n ')

    resposta = str(input('')).strip().upper()

    if resposta != 'F' and resposta != 'M':
        print(' \nresposta inválida, tente novamente')
        
print(' \nfim')
