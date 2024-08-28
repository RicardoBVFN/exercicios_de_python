print('alistamento obrigatório')
ano = int(input('digite o ano em que você nasceu: '))
print(' ')
idade = 2024 - ano
if idade == 18:
    print('meus parabéns, você foi selecionado para servir em cabrobó por um ano, SELVA!')
else:
    if idade < 18:
        print('que pena que as crianças que nem você não podem servir')
        print('ainda faltam {} ano(s) para seu serviço' .format(18 - idade))
    else:
        if idade > 18:
            print('era para você ter se apresentado a {} ano(s)' .format(idade - 18))
            print('você se alistou no período regular? (digite sim ou não)')
            resposta = str(input('')).strip().upper()
            if 'SIM' == resposta:
                print('ok, você está liberado')
            else:
                print('já rastreamos seu CPF, estamos indo atrás de você, boa sorte')
print(' ')
print('tenha um ótimo dia cidadão')
