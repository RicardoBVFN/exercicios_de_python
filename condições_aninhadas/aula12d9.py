print('controlador de preços \n ')
valor = float(input('digite o valor do produto: R$'))
opção_de_pagamento = int(input("""digite a forma de pagamento:
[1] à vista no dinheiro
[2] à vista no cartão
[3] parcelado no cartão
[4] fiado

"""))
print(' ')
if opção_de_pagamento == 1:
    print('como você escolheu pagar à vista no dinheiro, o valor do produto receberá um desconto de 10% \no total a pagar passa de R${:.2f} para R${:.2f}' .format(valor, (valor * 0.9)))
else: 
    if opção_de_pagamento == 2:
        print('como você escolheu pagar à vista no cartão, o valor do produto receberá um desconto de 5% \no total a pagar passa de R${:.2f} para R${:.2f}' .format(valor, (valor * 0.95)))
    else:
        if opção_de_pagamento == 3:
            n_parcelas = int(input('em quantas vezes você gostaria de parcelar? (para um pagamento com mais de duas parcelas é aplicado uma taxa de juros sobre o valor do \nproduto): '))
            if n_parcelas == 2:
                print('como você escolheu parcelar em duas vezes no cartão, você pagará o valor integral do produto \nsendo este de R${:.2f}' .format(valor))
            else:
                print('como você escolheu dividir o valor em {} vezes, você pagará o valor integral acrescido de uma taxa de juros de 20%\nsaindo de R${:.2f} para R${:.2f}' .format(n_parcelas, valor, (valor * 1.2)))
        else:
            if opção_de_pagamento == 4:
                print('fiado apenas para pessoas acima de 80 anos acompanhados dos avós')
            else:
                print('opção inválida, tente novamente')