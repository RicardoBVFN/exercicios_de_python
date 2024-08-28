print('analista de notas com dicionários')

# declaração do dicionário
cadastro_do_aluno = {}

# coleta dos dados do aluno
nome_do_aluno = str(input('\ndigite o nome do aluno: ')).strip()

media_do_aluno = str(input('digite a média do aluno: ')).strip()

# adição do nome e da média do aluno no dicionário
cadastro_do_aluno['nome'] = nome_do_aluno
cadastro_do_aluno['média'] = media_do_aluno

# verificação e adição da situação do aluno no dicionário
if float(media_do_aluno) >= 7:
    cadastro_do_aluno['situação'] = 'aprovado'

else:
    cadastro_do_aluno['situação'] = 'reprovado'

# exibição dos resultados
print(f'\no aluno {cadastro_do_aluno["nome"]} possui a média de {cadastro_do_aluno["média"]}\n\nele está {cadastro_do_aluno["situação"]}')

