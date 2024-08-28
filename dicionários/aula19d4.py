print('\n\nanalista de rendimento de um jogador de futebol com dicionários')

dicionario = {}
temp_list = []
main_list = []
soma_de_gols = 0

dicionario['nome do jogador'] = str(input('digite o nome do jogador: ')).strip().upper()

dicionario['numero de partidas jogadas'] = int(input('digite o número de partidas jogadas por esse jogador: '))

for c in range(0, dicionario['numero de partidas jogadas']):

    temp_list.append(int(input(f'digite quantos gols {dicionario["nome do jogador"]} fez na partida em sua {c + 1}º partida: ')))

    main_list.append(temp_list[:]) 

    temp_list.clear()

dicionario['número de gols por partida'] = main_list

for glos in main_list:

    soma_de_gols += glos[0]

dicionario['total de gols marcados'] = soma_de_gols

print(f'\n{dicionario}\n')

for key in dicionario:

    print(f'o valor de {key} é {dicionario[key]}')

