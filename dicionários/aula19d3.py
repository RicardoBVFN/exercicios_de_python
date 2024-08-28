dicionario = {}

dicionario['nome'] = str(input('\ndigite o seu nome: ')).strip().upper()
dicionario['data de nascimento'] = str(input('digite sua data de nascimento: ')).strip()
dicionario['idade'] = 2024 - int(dicionario['data de nascimento'])
dicionario['carteira de trabalho'] = str(input('digite o número da sua carteira de trabalho (digite 0 se não possuir): '))

if dicionario['carteira de trabalho'] != '0':
    dicionario['ano de contratação'] = str(input('digite o ano em que você foi contratado: ')).strip()
    dicionario['ano da aposentadoria'] = int(dicionario['ano de contratação']) + 35

for x in dicionario:

    print(f'o valor de {x} é {dicionario[x]}')