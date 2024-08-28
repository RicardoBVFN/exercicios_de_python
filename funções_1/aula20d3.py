print('\n\ncontador com funções')


def contagem(início, fim, método):

    if método != 0:
        for c in range(início, (fim + 1), método):

            print(f'{c} ', end='')
    
    else:
        for c in range(início, (fim + 1)):

            print(f'{c} ', end='')
            if c == fim:

                print('FIM')


inicio = int(input('digite um valor inteiro positivo para ser o início da função: '))

fim = int(input('digite um valor inteiro positivo para ser o fim da função: '))

metodo = int(input('selecione o método que será daotado na contagem\n\n[2] conta de 2 em 2\n[0] contagem normal\n[-1] contagem referça\n\n'))

contagem(inicio, fim, metodo)
