print('tipificador numérico')
number = float(input('digite um número inteiro: '))
print("""
""")
if (number % 2) == 0:
    print('este número é par')
else:
    if (number % 2) == 1:
        print('este número é impar')
    else:
        print('este número não é inteiro')
        