maiores = 0
menores = 0
for c in range(1, 8):
    ano_nanscimento = int(input('digite o ano que você nasceu: '))
    idade = 2024 - ano_nanscimento
    if idade >= 18:
        maiores = maiores + 1
    else: 
        menores = menores +1
print(' \ndessas sete pessoas, {} são maiores de idade e {} são menores de idade' .format(maiores, menores))