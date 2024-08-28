print('jogos para a mega sena')

lista_de_jogos = []
lista_temporaria = []
import random

# definição do número de jogos a serem gerados
quantidade_de_jogos = int(input('\ndigite a quantidade de jogos que você deseja gerar: '))

# laço principal do programa 
for c in range(0, quantidade_de_jogos):

    print(f'\njogo {c + 1}: ', end='')

    # sorteio dos números e criação dos jogos
    while True:
        numero = random.randint(1, 60)
        if numero not in lista_temporaria:
            lista_temporaria.append(numero)
        if len(lista_temporaria) >= 6:
            break
    lista_de_jogos.append(lista_temporaria[:])
    lista_temporaria.clear()

    print(lista_de_jogos[c])
