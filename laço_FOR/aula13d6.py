print('calculadora de P.A\n ')
a1 = float(input('digite um número qualquer para ser o primeiro termo da P.A: '))
k = float(input('digite um número quaquer para ser a razão da P.A: '))
n = int(input('digite a quantidade de termos da sua P.A: '))
for c in range(0, n):
    print(' ')
    a = a1 + (k * c)
    print('a{} = {}' .format((c + 1), a))
