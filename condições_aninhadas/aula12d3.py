print('comparador de números')
n1 = float(input('digite o primeiro número: '))
n2 = float(input('digite o segundo número: '))
print("""
""")
if n1 > n2:
    print('o maior número é {}' .format(n1))
else: 
    if n2 > n1:
        print('o maior número é {}' .format(n2))
    else:
        print('os números são iguais')
