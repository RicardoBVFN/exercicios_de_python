print('avaliador de para financiamentos')
salario = float(input('digite o seu salário: R$'))
valor = float(input('digite o valor do financiamento: R$'))
periodo = int(input('digite o período do financiamento (em mêses):'))
print("""
""")
prestacao = valor / periodo
if prestacao > (salario * 0.3):
    print('lamento, mas seu financiamento foi recusado')
else:
    print('de acordo, seu financiamento de R${:.2f} será pago em {:.0f} prestações de R${:.2f}, digite sim se concorda com esses termos' .format(valor, periodo, prestacao))
    resposta = str(input('')).upper()
    if 'SIM' == resposta:
        print('meus parabéns, você acaba de aprovar o seu financiamento')
    else:
        print('que pena, espero poder fazer negócios com você posteriormente')
print('tenha um ótimo dia!')
