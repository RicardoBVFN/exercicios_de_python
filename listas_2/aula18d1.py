print('analista de dados com listas complexas')

# decalaração de listae e variaveis
main_list = []
data_list = []
cont = 0
most_hevy = 0
most_light = 0

# laço principal do programa 
while True:

    #coleta e validação do nome do usuário
    while True:
        user_name = str(input('\ndigite o seu nome: ')).strip()
        if user_name != '':
            break
        print('\nvocê deve digitar o seu nome para prosseguir, tente novamente')

    data_list.append(user_name)

    #coleta e validação do peso do usuário
    while True:
        user_weigh = str(input('digite o seu peso em Kg (utilise "." no lugar da ","): ')).strip()
        if user_weigh != '' and ',' not in user_weigh:
            break
        print('\nvocê deve digitar um valor válido para o seu peso, tente novamente\n')

    data_list.append(float(user_weigh))

    # processamento de dados para definição do usuário mais pesado e mais leve
    if cont == 0:
        most_hevy = data_list[1]
        most_light = data_list[1]
    else:
        if most_hevy < data_list[1]:
            most_hevy = data_list[1]

        if most_light > data_list[1]:
            most_light = data_list[1]

    main_list.append(data_list[:])

    data_list.clear()

    # verificação e validação da resposta do usuário quanto ao prossegmento ou interrupção do programa
    while True:
        user_choise = str(input('\ndeseja continuar?\n\n[1] sim\n[2] não, encerrar programa\n\n')).strip()
        if user_choise in ('1', '2'):
            break
        print('\nresposta inválida, tente novamente')

    if user_choise == '2':
        break

    cont += 1

# exposção do número de usuários cadastrados
print(f'\num total de {len(main_list)} usuários foram cadastrados')

# exposição do(s) usuário(s) mais pesado(s)
print('\no(s) usuário(s) mais pesado(s) foi(foram): ', end='')

n_most_hevy = 0

for x in main_list:
    for y in x:
        if y == most_hevy:
            n_most_hevy += 1

cont_most_hevy = 0

for c in main_list:
    if c[1] == most_hevy:
        print(c[0], end='')
        cont_most_hevy += 1
        if n_most_hevy > 1:
            if n_most_hevy == cont_most_hevy:
                print(f'. Todos com {most_hevy}Kg')
            else:
                if cont_most_hevy == n_most_hevy - 1:
                    print(' e ', end= '')
                else:
                    print(', ', end='')
        else:
            print(f', com {most_hevy}Kg')

# exposição do(s) usuário(s) mais leve(s)
print('o(s) usuário(s) mais leve(s) foi(foram): ', end='')

n_most_light = 0

for x in main_list:
    for y in x:
        if y == most_light:
            n_most_light += 1

cont_most_light = 0

for c in main_list:
    if c[1] == most_light:
        print(c[0], end='')
        cont_most_light += 1
        if n_most_light > 1:
            if n_most_light == cont_most_light:
                print(f'. Todos com {most_light}Kg')
            else:
                if cont_most_light == n_most_light - 1:
                    print(' e ', end= '')
                else:
                    print(', ', end='')
        else:
            print(f', com {most_light}Kg')
