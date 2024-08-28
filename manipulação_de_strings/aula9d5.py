print('quantos "a"')
frase = (str(input('digite uma frase: '))).strip().upper()
frase_split = frase.split()
frase_organizada = ' '.join(frase_split)
print("""
""")
n_a = frase_organizada.count('A')
print('essa frase possui {} letras "a"' .format(n_a))
print("""
""")
p_a = frase_organizada.find('A') + 1
print('a primeira letra "a" desta frase aparece na posição de número {}' .format(p_a))
print("""
""")
u_a = frase_organizada.rfind('A') + 1
print('a última letra "a" aparece na posição de número {}' .format(u_a))
