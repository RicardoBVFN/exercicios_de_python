print('analisador de textos')
frase_1 = input('digite seu nome: ')
print("""
""")
frase_split = frase_1.split()
frase_organizada = ' '.join(frase_split)
print('O texto escrito em maiúsculo é: {}' .format(frase_organizada.upper()))
print("""
""")
print('O texto escrito em minúsculo é: {}' .format(frase_organizada.lower()))
print("""
""")
primeiro_nome_lenth = len(frase_split[0])
print('A primeira palavra do seu texto possui {} caracteres' .format(primeiro_nome_lenth))
print("""
""")
frase_concatenada = ''.join(frase_split)
n_caracteres_frase = len(frase_concatenada)
print('Desconsideranso os espaços, o texto possui {} caracteres ao total'.format(n_caracteres_frase))
