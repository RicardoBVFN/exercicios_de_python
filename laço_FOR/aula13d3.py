print('soma de todos os números inteiros\nmúltiplos de 3\ne ímpares\n ')
soma = 0
for c in range(1, 501):
    if c % 3 == 0 and c % 2 == 1:
        soma = soma + c
print(soma)