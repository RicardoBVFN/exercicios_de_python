print('\n\nanalista numérico simples com funções')

def maior(lista_inserida):

    maior_valor = 0
    cont = 0

    while cont < len(lista_inserida):

        if cont == 0:

            maior_valor = lista_inserida[0]

        else:

            if maior_valor < lista_inserida[cont]:

                maior_valor = lista_inserida[cont]

        cont += 1

    print(f'\no maior valor da lista inserida é {maior_valor}')

lista_numeros = []

while True:

    numero = int(input('\ndigite um valor inteiro para ser comparado'))

    lista_numeros.append(numero)

    resposta_do_usuario = str(input('deseja cadastrar mais algum número?\n\n[1] sim\n[2] não, encerrar programa\n\n')).strip()

    if resposta_do_usuario == '2':

        break

maior(lista_numeros)
