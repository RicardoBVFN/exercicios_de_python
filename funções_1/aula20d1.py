print('\ncálculo de área com funções')


def area(largura, comprimento):

    area = largura * comprimento

    print(f'\na área da da figura em questão é {area}')


largura = int(input('\ndigite a largura da sua figura: '))

comprimento = int(input('digite o comprimento da sua figura: '))

area(largura, comprimento)