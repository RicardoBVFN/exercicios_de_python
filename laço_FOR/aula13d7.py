print('sua frase é um plíndromo?\n ')
frase = str(input('digite uma frase qualquer: ')).strip().upper()
frase_split = frase.split()
frase_concatenada = ''.join(frase_split)
if (frase_concatenada[(len(frase_concatenada)):0:-1] + frase_concatenada[0]) == frase_concatenada:
    print(' \nessa frase é um palíndromo')
else:
    print(' \nessa frase não é um palíndromo')
