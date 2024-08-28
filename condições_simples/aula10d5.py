year = int(input('digite um ano qualquer: '))
print("""
""")
if year % 100 != 0 and year % 4 == 0 or year % 400 == 0:
    print('esse ano é bisexto')
else:
    print('esse ano não é bisexto')
