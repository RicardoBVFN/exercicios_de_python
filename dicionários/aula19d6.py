print('\nrendimento de  jogadores de futebol')

#declaração de variáveis
lista_jogadores_cadastrados = []
perfil_jogador = []
numero_gols_partidas = []
total_de_gols = 0

while True:

    while True:
        nome_do_jogador = str(input('\ndigite o nome do jogador a ser cadastrado: ')).strip().upper()

        if nome_do_jogador != '':
            break

        print('\nvocê deve digitar o nome do jogador para proceguir, tente novamente')

    perfil_jogador.append(nome_do_jogador)

    while True:
        numero_de_partidas_jogadas = int(input('digite a quantidade de partidas jogadas por este jogador: '))

        if numero_de_partidas_jogadas > 0:
            break

        print('\nvocê deve digitar um valor válido para a quantidade de partidas jogadas, tente novamemte\n')

    perfil_jogador.append(numero_de_partidas_jogadas)

    print()

    for partida in range(0, numero_de_partidas_jogadas):

        numero_de_gols = int(input(f'digite a quantidade de gols marcados por {perfil_jogador[0]} em sua {partida + 1}ª partida: '))

        total_de_gols += numero_de_gols

        numero_gols_partidas.append(numero_de_gols)

    perfil_jogador.append(numero_gols_partidas[:])

    perfil_jogador.append(total_de_gols)

    lista_jogadores_cadastrados.append(perfil_jogador[:])

    perfil_jogador.clear()

    numero_gols_partidas.clear()

    total_de_gols = 0

    while True:

        resposta_do_usuario = str(input('\ndeseja cadastrar algum outro jogador?\n\n[1] sim\n[2] não, encerrar cadastro\n\n'))

        if resposta_do_usuario in ('1', '2'):
            break

        print('\nresposta inválida, tente novamente')

    if resposta_do_usuario == '2':
        break

print('\n', '-' * 15, 'atletas cadastrados', '-' * 15, '\n')

print(f'{'número':<5}{'nome':^11}{'n.partidas':^5}  {'total de gols':5>}')

for jogador in lista_jogadores_cadastrados:

    print(f'{lista_jogadores_cadastrados.index(jogador):<5}{jogador[0]:^11}   {jogador[1]:^5}           {jogador[3]:5>}')

while True:

    resposta_do_usuario2 = str(input('\ndeseja consultar os resultados individuais de algum jogador cadastrado?\n\n[1] sim\n[2] não, encerrar programa\n\n')).strip()

    if resposta_do_usuario2 in ('1', '2'):
        break

    print('resposta inv´lida, tente novamente')

if resposta_do_usuario2 == '1':

    while True:

        while True:
            numero_de_consulta = str(input('\ndigite o número de cadastro do jogador o qual deseja consultar os dados\n\n')).strip()

            numero_de_consulta = int(numero_de_consulta)

            if numero_de_consulta in range(0, len(lista_jogadores_cadastrados)):

                break

            print('\nnúmero de cadastro inválido, tente novamente')

        print(f'o jogador {lista_jogadores_cadastrados[numero_de_consulta][0]} teve o seguinte desempenho individual:\n')
        for gols in lista_jogadores_cadastrados[numero_de_consulta][2]:

            print(f'em sua {gols}ª partida, {lista_jogadores_cadastrados[numero_de_consulta][0]} fez {lista_jogadores_cadastrados[numero_de_consulta][2][gols - 1]} gols')

        while True:
            resposta_do_usuario3 = str(input('\ndeseja consultar os dados de mais algum jogador?\n\n[1] sim\n[2] não, encerrar programa\n\n')).strip()

            if resposta_do_usuario3 in ('1', '2'):
                break

        if resposta_do_usuario3 == '2':
            break

print('\nobrigado por utilisar o rendimento de  jogadores de futebol que era pra ser com dicionário mas eu vou fazer com listas porque sim, boa sorte no XD')

