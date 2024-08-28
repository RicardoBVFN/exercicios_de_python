print('somatório dos pares\n ')
soma_pares = 0
for c in range(1, 7):
    n = int(input('digite um número inteiro qualquer: '))
    if n % 2 == 0:
        soma_pares = soma_pares + n
print(' \ndesconsiderando os números ímpares, a soma dos termos acima corresponde a {}' .format(soma_pares))
