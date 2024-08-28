import random

print('estou pensando em um número inteiro de 0 à 5, que número é esse?')
print("""
""")
from random import randint
n = random.randint(0,5)
resposta = int(input('digite seu palpite: '))
print("""
""")
print('o número que eu estava pensando era {}' .format(n))
print("""
""")
if resposta == n:
    print('parabéns, você acertou :)')
else:
    if resposta >= 6 or resposta <= (-1):
        print('tu é burro em?!')
    else:
        print('lamento, mas não foi dessa vez XD')
