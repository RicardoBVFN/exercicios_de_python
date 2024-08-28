print('seu primeiro e último nome')
nome = str(input('digite o seu nome: ')).strip().title()
print("""
""")
nome_split = nome.split()
print('seu primeiro nome é: {}' .format(nome_split[0]))
print("""
""")
ultimo_nome = nome_split[len(nome_split) - 1]
print('seu último nome é: {}' .format(ultimo_nome))
