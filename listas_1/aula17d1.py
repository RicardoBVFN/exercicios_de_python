print('analista numérico listas\n')

lista_valores = []
posicao_maior_valor = []
posicao_menor_valor = []

# input de valores na lista 
for c in range(0, 5):
    lista_valores.append(int(input('digite um valor inteiro qualquer: ')))

    if c == 0:
        maior_valor = lista_valores[c]
        menor_valor = lista_valores[c]
        posicao_maior_valor.append(c)
        posicao_menor_valor.append(c)
    else:

# maior valor
        if maior_valor == lista_valores[c]:
            posicao_maior_valor.append(c)
        if maior_valor < lista_valores[c]:
            maior_valor = lista_valores[c]
            for x in range(0, len(posicao_maior_valor)):
                posicao_maior_valor.pop()
            posicao_maior_valor.append(c)
    
# menor valor  
        if menor_valor == lista_valores[c]:
            posicao_menor_valor.append(c)
        if menor_valor > lista_valores[c]:
            menor_valor = lista_valores[c]
            for x in range(0, len(posicao_menor_valor)):
                posicao_menor_valor.pop()
            posicao_menor_valor.append(c)

# prints
print(f'\no maior valor digitado foi {maior_valor}, na posição {posicao_maior_valor}')

print(f'o menor valor digitado foi {menor_valor}, na posição {posicao_menor_valor}')
