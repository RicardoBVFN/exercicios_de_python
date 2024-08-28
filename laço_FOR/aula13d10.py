print('analista completo\n ')
mais_velho = ''
soma_idade = 0
mulheres_menos_de_20 = 0
idade_mais_velho = 0
for c in range(1, 5):
    nome = str(input('digite o seu nome: ')).strip().title()
    idade = int(input('digite a sua idade: '))
    sexo = str(input('digite seu sexo:\n[m] masculino\n[f] feminino\n')).strip().upper()
    soma_idade = soma_idade + idade
    if c == 1 and sexo == 'M':
        mais_velho = nome
        idade_mais_velho = idade
    else:
        if sexo == 'M' and idade > idade_mais_velho:
            mais_velho = nome
            idade_mais_velho = idade
    if sexo == 'F' and idade < 20:
        mulheres_menos_de_20 = mulheres_menos_de_20 + 1
media_grupo = soma_idade / 4
print(' \no nome do homem mais velho é {}, com {} anos\n{} mulheres tem menos de 20 anos\na media de idade do grupo é {:.1f}' .format(mais_velho, idade_mais_velho, mulheres_menos_de_20, media_grupo))    
