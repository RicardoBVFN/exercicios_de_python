print('-' * 40)
print(f'{'lista de compras':^40}')
print('-' * 40)
lista_de_compras = ('pão', 5.50, 'suco', 28.90, 'queijo', 5.60, 'salmão', 13.7)
for x in range(0, len(lista_de_compras)):
    if x % 2 == 0:
        print(f'{lista_de_compras[x]:.<30}', end = '')
    else: 
        print(f'R${lista_de_compras[x]:>5.2f}')
