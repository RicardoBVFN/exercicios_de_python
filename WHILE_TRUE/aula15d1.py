print('leitor numérico break')
soma = 0
cont = 0
while True:
    user_input = float(input(' \ndigite um número qualquer: '))
    if user_input == 999:
        break
    soma = soma + user_input
    cont = cont + 1
print(f' \nsua sequencia contou com {cont} elementos, que somados resultam em {soma}')
