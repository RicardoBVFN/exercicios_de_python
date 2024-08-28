print('\nboletin completo')

# declaração das listas
main_list = []
data_list = []

# laço principal do programa
while True:

    # coleta e validação do nome do aluno a ser cadastrado
    while True:
        student_name = str(input('\ndigite o nome do aluno:')).strip()
        if student_name != '':
            break
        print('o nome do aluno deve ser digitado para proceguir com o cadastro, tente novamente')

    data_list.append(student_name)

    # coleta e validação da nota do aluno na primeira avaliação
    while True:
        student_note_1 = str(input('digite a nota do aluno na primeira avaliação: ')).strip()
        if student_note_1 != '':
            break
        print('\numa nota válida para a primeira avaliação deve ser digitada, tente novamente\n')

    data_list.append(student_note_1)

    # coleta e validação da nota do aluno na segunda avaliação
    while True:
        student_note_2 = str(input('digite a nota do aluno na primeira avaliação: ')).strip()
        if student_note_2 != '':
            break
        print('\numa nota válida para a segunda avaliação deve ser digitada, tente novamente\n')

    data_list.append(student_note_2)

    # cálculo e adição da média ao cadastro
    media = (float(student_note_1) + float(student_note_2)) / 2

    data_list.append(media)

    # adição do perfil cadastrado à lista principal e rebut da lista secundária
    main_list.append(data_list[:])
    data_list.clear()

    # coleta e validação da resposta do usuário quanto à posseguição ou interrupção do programa
    while True:
        user_choise = str(input('\ndeseja continuar?\n\n[1] sim\n[2] não, encerrar processo de cadastro\n\n')).strip()

        if user_choise != '' and (user_choise == '1' or user_choise == '2'):
            break

        print('\nresposta inválida, tente novamente')

    # interrupção do programa
    if user_choise == '2':
        break

print('\n', '-' * 15, 'notas', '-' * 15, '\n')
print(f'\n[{'número '}] [{'nome do aluno cadastrado '}] [{'média'}]\n\n')

for c in range(0, len(main_list)):
    print(f'{c:^8} {main_list[c][0]:^27} {main_list[c][3]:>6}')

# coleta e validação da resposta do usuário quanto a exibição ou não das notas individualmente
while True:
    user_choise2 = str(input('\ndeseja consultar a nota de algum aluno individualmente?\n\n[1] sim\n[2] não, encerrar programa\n\n')).strip()
    
    if user_choise != '' and (user_choise == '1' or user_choise == '2'):
        break

    print('\nresposta inválida, tente novamente')

# exibição de notas
if user_choise2 == '1':

    while True:

        # coleta e validação do número do aluno
        while True:
            user_choise3 = str(input('\ndigite o número correspondene ao aluno cujas notas individuais serão exibidas: ')).strip()

            if user_choise3 != '':
                break

            print('\nresposta inválida, tente novamente')
        
        print(f'\na nota de {main_list[int(user_choise3)][0]} foram\n\nAV1: {main_list[int(user_choise3)][1]}\nAV2: {main_list[int(user_choise3)][2]}')

        while True:
            user_choise4 = str(input('\ndeseja consultar as notas de algum outro aluno?\n\n[1] sim\n[2] não, encerrar programa\n\n')).strip()

            if user_choise != '' and (user_choise == '1' or user_choise == '2'):
                break

            print('\nresposta inválida, tente novamente')

        if user_choise4 == '2':
            break

print('\nobrigado por usar o boletin completo, boa sorte no  XD')
