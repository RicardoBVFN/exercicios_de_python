print('comparador numérico, ordem de grandeza')
n1 = float(input('digite um número: '))
n2 = float(input('digite outro número: '))
n3 = float(input('digite mais um número:'))
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('o maior valor é {}' .format(maior))
menor = n3
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
print('o menor valor é {}' .format(menor))
