print('calculador de tabuada 3.0')
while True:
    user_input = float(input(' \ndigite um número inteiro positivo para ser multiplicado (numeros negativos ou fracionados resultarão na interrupção do programa): '))
    if user_input < 0 or (user_input % 2 != 0 and user_input % 2 != 1):
        print(' \nlamento, mas numeros negativos ou fracionados não serão aceitos. reinicie e tente novamente')
        break
    user_range = int(input(' \ndigite quantas vezes você deseja que seu número seja multiplicado (a regra acima ainda se mantém): '))
    if user_range < 0:
        print(' \nlamento, mas numeros negativos ou fracionados não serão aceitos. reinicie e tente novamente')
        break
    for c in range(1, (user_range + 1)):
        print(f' \n{user_input:.0f} x {c} = {c * user_input:.0f}')
    user_choise = ''
    while user_choise != 'S' and user_choise != 'N':
        user_choise = str(input(' \ndeseja continuar?\n \n[s]sim\n[n]não, fechar programa\n \n')).strip().upper()
        if user_choise != 'S' and user_choise != 'N':
            print(' \nlamento, mas sua resposta é inválida. tente novamente')
    if user_choise == 'N':
        print(' \nobrigado por usar o calculador de tabuada 3.0, boa sorte no XD')
        break
    