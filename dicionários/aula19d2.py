print('\njogo de dados com dicionários')

# declaração das variáveis
jogo = []
jogador = {}
cont = 7
# importação da biblioteca
from random import randint

for c in range(1, 5):
    jogador['nome do jogador'] = str(input('digite o nome do jogador que vai jogar agora: ')).strip()
    jogador['jogada'] = randint(1, 6)
    jogo.append(jogador.copy())

jogo.sort(reverse=True)
    

print(jogo) 
