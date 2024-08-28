print('analista numérico com matrizes')

# declaração de variáveis
matriz = [[[], [], []], [[], [], []], [[], [], []]]
soma_pares = 0
soma_terceira_coluna = 0

# laço principal do programa
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'digite um valor para a linha {linha + 1}, coluna {coluna + 1}: '))

        if coluna == 2:
            print()

        # somatório dos elementos da terceira coluna
        if coluna == 2:
            soma_terceira_coluna += matriz[linha][2]

        #somat´rio dos elementos pares
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]

# exibição dos resultados
print('a matriz gerada foi:\n')

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()

print(f'\na soma dos números pares digitados é: {soma_pares}')

print(f'\na soma dos elementos da terceira coluna é: {soma_terceira_coluna}')

matriz[1].sort(reverse = True)

print(f'\no maior valor da segunda linha é: {matriz[1][0]}')
    