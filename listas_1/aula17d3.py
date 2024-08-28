print('analista numérico listas/while')

lista_valores = []

# laço
while True:

# veriicação do valor a ser adicionado
    while True:
        input_usuario = int(input('\ndigite um valor interio: '))
        if lista_valores.count(input_usuario) == 0:
            break
        print('\nvalores repetidos não serão adicionados, tente novamente')

# adição do valor verificado à lista 
    lista_valores.append(input_usuario)
    print('\nnovo valor adicionado comm sucesso')

# verificação da continuidade ou não do programa
    while True:
        decisao_usuario = int(input('\ndeseja continuar?\n\n[1] sim\n[2] não, encerrar programa\n\n'))
        if decisao_usuario in (1, 2):
            break
        print('\nresposta inválida, tente novamente')
    if decisao_usuario == 2:
        break

# exibição do resultado
lista_valores.sort()
print(f'\nos valores digitados, organizados em ordem crescente, foram: {lista_valores}')