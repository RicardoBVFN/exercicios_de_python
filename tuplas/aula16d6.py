print('contador de vogais tupla')
tupla = ('eu', 'odeio', 'tuplas', 'vai', 'se', 'fuder')
for c in range(0, len(tupla)):
    print(f' \nas vogais da palavra {tupla[c]} são: ', end = '')
    for x in tupla[c]:
        if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
            print(x, end = ' ')