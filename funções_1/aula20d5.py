print('\n\nanalista de números sorteados com fuções')

# deffinição da função 'sorteio'
def sorteio(lista_inserida, n_numeros):

    from random import randint

    for c in range(0, n_numeros):

        numero_sorteado = randint(1, 100)

        lista_inserida.append(numero_sorteado)

# definição da função 'soma_paares'
def soma_pares(lista_inserida):

    somatorio = 0

    for c in lista_inserida:

        if c % 2 == 0:

            somatorio += c

    print(f'\na soma dos elementos pares dessa lista é {somatorio}')


lista_qualquer = []

numero_de_numeros_sorteados = int(input('\ndigite a quantodade de elementos que serão sorteados: '))

# aplicação da função 'sorteio'
sorteio(lista_qualquer, numero_de_numeros_sorteados)

print(f'\nos números sorteados foram: {lista_qualquer}')

# aplicação da função 'soma_pares'
soma_pares(lista_qualquer)
