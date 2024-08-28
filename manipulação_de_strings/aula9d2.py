print('decompositor numérico')
numero = int(input('digite um número inteiro de 0 a 9999: '))
unidades = (numero % 10)
print('este número possui:')
print("""
""")
print('{:.0f} unidades' .format(unidades))
dezenas = numero // 10 % 10
print('{:.0f} dezenas' .format(dezenas))
centenas = numero // 100 % 10
print('{:.0f} centenas' .format(centenas))
unidades_milhar = numero // 1000 % 10
print('{:.0f} unidades de milhar' .format(unidades_milhar))
