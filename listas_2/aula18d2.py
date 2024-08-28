print('analista numperico com listas compostas\n')

main_list = [[], []]

#laço principal do programa
for c in range(0, 7):

    #coleta e validação do input do usuário
    user_input = int(input('digite um valor: '))
    
    if user_input % 2 == 0:
        main_list[0].insert(0, user_input)
    else:
        main_list[1].insert(0, user_input)

# exibição dos pares
pares_ordenados = main_list[0].sort()

print(f'\nos valores pares digitados foram: {main_list[0]}')

# exibição dos ímpares
impares_ordenados = main_list[1].sort()

print(f'os valores ímapares digitados foram: {main_list[1]}')