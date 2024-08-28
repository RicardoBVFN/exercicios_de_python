print('\nformatador de textos com funções')

def frase_formatada(frase, icone):

    print('\n', '-' * 15, 'frase formatada', '-' * 15, '\n')
    print(icone * (len(frase) + 2))
    print(f'{frase:^}')
    print(icone * (len(frase) + 2), '\n')


frase = str(input('\ndigite uma frase para ser formatada: '))

icone = str(input('digite o ícone que formatará a frase: '))

frase_formatada(frase, icone)