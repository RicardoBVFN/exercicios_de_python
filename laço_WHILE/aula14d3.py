print('calculadora basicona\n ')

user_choise = 0
resposta = 0

while user_choise != 5:

    user_choise = int(input('escolha qual operação deseja realizar\n \n[1] soma\n[2] subtração\n[3] multiplicação\n[4] divisão\n[5] sair do programa\n \n'))

    if user_choise != 5:
        n1 = float(input(' \ndigite o primeiro número: '))
        n2 = float(input('digite o segundo número: '))

        if user_choise == 1:
            resposta = n1 + n2
            print(' \n{} + {} = {}' .format(n1, n2, resposta))

        if user_choise == 2:
            resposta = n1 - n2
            print(' \n{} - {} = {}' .format(n1, n2, resposta))

        if user_choise == 3:
            resposta = n1 * n2
            print(' \n{} x {} = {}' .format(n1, n2, resposta))

        if user_choise == 4:
            resposta = n1 / n2
            print(' \n{} / {} = {}' .format(n1, n2, resposta))
            
print(' \nobrigado por usar a calculadora basicona, boa sorte no XD')
