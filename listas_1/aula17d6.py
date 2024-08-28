print('separando pares de ímpares')

lista_defoult = []
#laço da primeira lista
while True:
    lista_defoult.append(int(input('\ndigite um valor inteiro qualquer: ')))

# leitura e validação da resposta do usuário
    while True:
        user_choise = str(input('\ndeseja continuar?\n\n[1] sim\n[2] não, fechar programa\n\n'))
        if user_choise in ('1', '2'):
            break
        print('\nresposta inválida, tente novamente')

    if user_choise == '2':
        break

# pares
lista_pares = []
for x in lista_defoult:
    if x % 2 == 0:
        lista_pares.append(x)

# ímpares
lista_impares = []
for y in lista_defoult:
    if y % 2 == 1:
        lista_impares.append(y)

# print resultados
print(f'a lista digitada foi {lista_defoult}\n\nos números pares digitados foram {lista_pares}\nos números ímpares digitados foram {lista_impares}')