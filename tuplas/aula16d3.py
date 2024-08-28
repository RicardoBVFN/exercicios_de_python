from random import randint
n1 = randint(0, 9)
n2 = randint(0, 9) 
n3 = randint(0, 9)
n4 = randint(0, 9)
n5 = randint(0, 9)
tabela = (n1, n2, n3, n4, n5)
print(f' \nos número sorteados foram {tabela} \no maior número sorteado foi {sorted(tabela)[-1]}\no menor número sorteado foi {sorted(tabela)[0]}\no número 9 apareceu {tabela.count(9)} vezes')
