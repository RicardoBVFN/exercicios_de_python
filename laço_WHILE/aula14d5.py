print('calcukadora de P.A 2.0\n ')

a1 = float(input('digite um valor qualquer para representar o primeiro termo de uma P.A: '))
k = float(input('digite um valor qualquer para representar a rasão dessa P.A: '))
n = int(input('digite quantos termos essa P.A terá: '))

nx = 0
a = 0

while nx != n:

    nx += 1

    if nx == 1:
        a = a1

    else:
        a = a1 + ((nx - 1) * k)

    print(' \na{} = {}' .format(nx, a))
    
print(' \nfim')
