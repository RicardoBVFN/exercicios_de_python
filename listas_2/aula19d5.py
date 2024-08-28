# declaração de variáveis
lista_pessoas_cadastradas = []
lista_perfil_usuário = []
lista_pessoas_acima_da_idade = []
lista_mulheres_cadastradas = []
somatorio_das_idades = 0
media_idades = 0

# laço principal do programa
while True:

    # coleta e veridicação do nome do usuário
    while True:
        nome_usuario = str(input('\ndigite o nome do usuário: ')).strip().upper()

        if nome_usuario != '':
            break

        print('\nvocê deve digitar o nome do usuário para proceguir, tente novamente')

    lista_perfil_usuário.append(nome_usuario)

    # coleta e veridicação da idade do usuário
    while True:
        idade_do_usuário = str(input('digite a idade do usuário: ')).strip()

        if idade_do_usuário != '':
            break

        print('\nvocê deve digitar a idade do usuário para proceguir, tente novamente\n')

    idade_do_usuário = int(idade_do_usuário)
    lista_perfil_usuário.append(idade_do_usuário)
    somatorio_das_idades += idade_do_usuário

    # coleta e veridicação do sexo do usuário
    while True:
        sexo_do_usuário = str(input('digite o sexo do usuário [M/f]: ')).strip().upper()

        if sexo_do_usuário in ('M', 'F'):
            break

        print('\nvocê deve digitar o sexo do usuário para continuar, tente novamente\n')

    if sexo_do_usuário == 'F':

        lista_mulheres_cadastradas.append(lista_perfil_usuário[:])

    lista_perfil_usuário.append(sexo_do_usuário)

    lista_pessoas_cadastradas.append(lista_perfil_usuário[:])

    lista_perfil_usuário.clear()

    # coleta e veridicação da decisão do usuário quanto a procegção ou interrupção do programa
    while True:
        resposta_do_usuario = str(input('\ndeseja cadastrar outro usuário?\n\n[1]sim\n[2]não\n\n')).strip()

        if resposta_do_usuario in ('1', '2'):
            break

        print('\nresposta inválida, tente novamente')

    if resposta_do_usuario == '2':
        break

# cálculo da média das idades    
media_idades = somatorio_das_idades / len(lista_pessoas_cadastradas)

for perfil in lista_pessoas_cadastradas:

    if perfil[1] > media_idades:

        lista_pessoas_acima_da_idade.append(perfil)

# exposição dos resultados
print('-' * 15, 'usuários cadastrados', '-' * 15)

for usuario in lista_pessoas_cadastradas:

    print(f'\nnúmero de cadastro do usuário: {lista_pessoas_cadastradas.index(usuario)}\nnome do usuário: {usuario[0]}\nidade do usuário: {usuario[1]}\nsexo do usuário: {usuario[2]}')

print('\n', '-' * 15, 'mulheres cadastradas', '-' * 15, '\n')

for mulher in lista_mulheres_cadastradas:

    print(f'{mulher[0]} com {mulher[1]} anos')

print('\n', '-' * 15, 'usuários acima da média cadastrados', '-' * 15, '\n')

for coroa in lista_pessoas_acima_da_idade: 

    print(f'{coroa[0]} com {coroa[1]} anos e do sexo {coroa[2]}')
