print('analista completo 2.0')
n_homens = 0
n_mais_18 = 0
n_mulheres_menos_20 = 0
user_input_age = -1
user_input_sex = ''
user_choise = ''
while True:
    while user_input_age < 0 or user_input_age > 130:
        user_input_age = int(input(' \ndigite a sua idade: '))
        if user_input_age < 0:
            print(' \nvalor inválido para a idade de uma pessoa, tente novamente')
        if user_input_age > 130:
            print(' \ne é a múmia kkkkkkkkkkkkk, tente novamente')
    while user_input_sex != 'M' and user_input_sex != 'F':
        user_input_sex = str(input(' \ndigite seu sexo\n \n[m]masculino\n[f]feminino\n \n')).strip().upper()
        if user_input_sex != 'M' and user_input_sex != 'F':
            print(' \nresposta inválida, tente novamente')
    if user_input_age > 18:
        n_mais_18 += 1
    if user_input_sex == 'M':
        n_homens += 1
    if user_input_sex == 'F' and user_input_age < 20:
        n_mulheres_menos_20 += 1
    while user_choise != 'S' and user_choise != 'N':
        user_choise = str(input(' \ndeseja continuar?\n \n[s]sim\n[n]não, fechar programa\n \n')).strip().upper()
        if user_choise != 'S' and user_choise != 'N':
            print(' \nresposta inválida, tente novamente')
    if user_choise == 'N':
        break
    user_input_age = -1
    user_input_sex = ''
    user_choise = ''
print(f' \n{n_mais_18} pessoas tem mais de 18 anos\n{n_homens} homens foram cadastrados\n{n_mulheres_menos_20} mulheres tem menos de 20 anos')
print(' \nobrigado por usar o analista completo 2.0, boa sorte no XD') 