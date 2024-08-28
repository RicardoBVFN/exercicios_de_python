print('tabela de calssificação do campeonato brasileiro de futebol')
tabela = ('Athletico-PR',	'Atlético-GO', 'Atlético-MG', 'Bahia', 'Botafogo', 'Corinthians', 'Criciúma', 'Cruzeiro', 'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza', 'Grêmio', 'Internacional', 'Juventude', 'Palmeiras', 'Red Bull Bragantino', 'São Paulo', 'Vasco da Gama', 'Vitória')
print(' \nos cinco primeiros colocados são:\n \n')
print('-' * 15)
for c in range(0, 5):
    print(f'{c + 1}° - {tabela[c]}')
print('-' * 15)
print(' \nos cinco últimos colocados são:\n \n')
print('-' * 15)
for c in range(1, 6):
    print(f'{c + 15}° - {tabela[c + 14]}')
print('-' * 15)
print(f' \na posição do fortaleza é: {tabela.index('Fortaleza') + 1}°')