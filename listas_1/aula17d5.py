print('lista basicona pro cara n desistir do curso')
lista = []

# laço de leitura e incerção
while True:
    lista.append(int(input('\ndigite um valor inteiro qualquer: ')))

    # leitura e validação da resposta do usuário
    while True:
        user_choise = str(input('\ndeseja continuar?\n\n[1] sim\n[2] não, encerrar programa\n\n'))
        if user_choise in ('1', '2'):
            break
        print('\nresposta inválida, tente novamente')

    if user_choise == '2':
        break

# número de elementos
print(f'\nsua lista possui {len(lista)} elementos')

# verificação e armazenamento do index de 5
lista_index_5 = []
pos = 0
cont = 0
for c in lista:
    if c == 5:
        lista_index_5.append(pos)
        cont += 1
    pos += 1

# prints do numero 5
if 5 in lista:
    print(f'\no número 5 apareceu {cont} vez(es), na(s) posição(ões) {lista_index_5} ')
else:
    print('\no número 5 não foi digitado')

# lista decrescente
lista.sort(reverse = True)
print(f'\n sua lista em ordem decrescente é {lista}')