print('calculaddora de P.A 3.0\n ')
a1 = float(input('digite um valor qualquer para representar o primeiro termo da P.A: '))
k = float(input('digte o valor que representará a razão da P.A: '))
a = 0
an = 0
n = 0
t = 0
user_choise = int(input('quantos termos dessa P.A você deseja ver? '))
n = user_choise
for c in range(1, (n + 1)):
    a = a1 + ((c-1) * k)
    print(' \na{} = {}' .format(c, a))
    if c == n:
        an = a
        t = c
while user_choise != 0:
    user_choise = int(input('quantos termos mais você deseja ver? digite [0] caso deseje sair do sistema: '))
    if user_choise != 0:
        n = user_choise
        for x in range(1, (n + 1)):
            a = an + (x * k)
            print(' \na{} = {}' .format((t + x), a))
            if x == n:
                an = a
                t = t + x
print(' \nobrigado por usar a calculadora de P.A 3.0, boa sorte no XD')
