print('pritótipo de arvore binária')
lista = []
for c in range(0, 5):
    user_input = int(input('digte um número inteiro qualquer: '))
    if c == 0 or user_input > lista[len(lista) - 1]:
        lista.append(user_input)
    else:
        for x in lista:
            if user_input <= x:
                lista.insert(lista.index(x), user_input)
                break
print(lista)