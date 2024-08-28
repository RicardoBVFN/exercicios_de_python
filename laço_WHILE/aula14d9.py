print('analista de dados 2.0')
cont = 0
soma = 0
maior = 0
menor = 0
user_choise = ''
while user_choise != 'N':
    user_input = int(input(' \ndigite um valor inteiro qualquer: '))
    if cont == 0:
        maior = user_input
        menor = user_input
    else:
        if maior < user_input:
            maior = user_input
        if menor > user_input:
            menor = user_input
    cont = cont + 1
    soma = soma + user_input
    user_choise = ''
    while user_choise != 'S' and user_choise != 'N':
        user_choise = str(input(' \ndeseja continuar?\n \n[s]sim\n[n]não\n \n')).strip().upper()
        if user_choise != 'S' and user_choise != 'N':
            print(' \nopção inválida, tente novamente')
media = soma / cont 
print(' \na média dos números digitados foi de {:.1f}\no maior valor foi de {}\no menor valor foi de {}' .format(media, maior, menor))
    