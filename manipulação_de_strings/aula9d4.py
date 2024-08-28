print('verificador de "Silvas"')
nome = str(input('digite o seu nome: ')).upper()
nome_split = nome.split()
validacao = 'SILVA' in nome_split
print('você é um "Silva"? {}' .format(validacao))
