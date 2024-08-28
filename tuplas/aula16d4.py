print('analista numérico tupla')
n1 = int(input(' \ndigite um valor interio qualquer: '))
n2 = int(input(' \ndigite um valor interio qualquer: '))
n3 = int(input(' \ndigite um valor interio qualquer: '))
n4 = int(input(' \ndigite um valor interio qualquer: '))
tupla = (n1, n2, n3, n4)
print(f' \no número 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f' \no número 3 apareceu pela rpimeira vez na posição {tupla.index(3)}')
print('os números pares dogotados foram:', end=' ')
for i in tupla:
    if i % 2 == 0:
        print(i, end=' ')
