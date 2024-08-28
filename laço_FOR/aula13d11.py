print('seu número é primo?\n ')
n = int(input('digite um número inteiro qualquer: '))
n_divisoes = 0
for c in range(1, (n + 1)):
    if n % c == 0:
        n_divisoes = n_divisoes + 1
if n_divisoes == 2:
    print('o número {} é primo' .format(n))
else:
    print('o número {} não é primo' .format(n))
