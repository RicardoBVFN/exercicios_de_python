print('somatório númerico\n ')
cont = 0
user_input = 0
soma = 0

while user_input != 999:

    if cont == 0:
        user_input = int(input('digite um valor inteiro qualquer para dar início ao somatório: '))

    else:
        user_input = int(input(' \ndigite outro número para ser acrescentado ao somatório (digite 999 caso queira encerrar a sequência): '))

    if user_input != 999:
        soma = soma + user_input
        cont = cont + 1
        
print(' \nsequência finalizada. sua sequência teve {} elementos e seu somatório correspode a {}' .format(cont, soma))
