print('=-' * 10)
print('operador de tabuada')
print('=-' * 10, '\n ')
x = int(input('digite o valor inteiro que será multiplicado: '))
y = int(input('digite até que número inteiro será a tabuada: '))
for c in range(1, (y + 1)):
    print('\n \n{} X {} = {}' .format(x, c, (x * c)))
