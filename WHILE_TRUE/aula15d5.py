print('lista de compras')
user_choise = ''
n_product_more_1000 = 0
cheepest_product_name = ''
cheepest_product_value = 0
count_products = 0
soma = 0
while True:
    product_name = str(input(' \ndigite o nome do produto: '))
    while True:
        product_value = float(input(' \ndigite o valor do produto: R$'))
        if product_value > 0:
            break
        print(' \nvalores negativos não serão tolerados, tente novamente')
    if count_products == 0:
        cheepest_product_value = product_value
    else:
        if cheepest_product_value > product_value:
            cheepest_product_value = product_value
            cheepest_product_name = product_name
    if product_value > 1000:
        n_product_more_1000 += 1
    soma += product_value
    count_products += 1
    while True:
        user_choise = str(input(' \ndeseja continuar?\n \n[s]sim\n[n]não, finalizar lista de compras\n \n')).strip().upper()
        if user_choise == 'S' or user_choise == 'N':
            break
        print(' \nresposta inválida, tente novamente')
    if user_choise == 'N':
        break
print(f' \nsua lista conta com {count_products} produtos\n{n_product_more_1000} produtos custam mais de R$1000.00\no produto mais barato é {cheepest_product_name} custando {cheepest_product_value}\no total a pagar é de R${soma:.2f}')
print('obrigado por usar a lista de compras, boa sorte no XD')
