print('\n\nstatus de obrigatoriedade de voto')


def voto(data_de_nascimento):
    
    idade = 2024 - data_de_nascimento

    if idade < 16:

        return 'não pode votar'

    if (idade >= 16 and idade < 18) or idade > 65:

        return 'possui voto facultativo'
    
    if idade >= 18:

        return 'deve votar obrigatoriamente'
    
def verificacao_frase_conteudo(frase_complementar):

    while True:

        user_input = str(input(f'\ndigite {frase_complementar}: ')).strip()

        if user_input != '':

            break

        print('\ndigitação inválida, tente novamente')

    return user_input

def verificacao_data_de_nascimento(frase_commplementar):

    while True:

        user_input = str(input(f'\ndigite {frase_commplementar}: ')).strip()

        if user_input != '':

            user_input = float(user_input)

            if user_input < 2024:

                break

            print('\ndigitação inválida, tente novamente')

        else:
            
            print('\ndigitação inválida, tente novamente')

    return user_input


nome_usuario = verificacao_frase_conteudo('o seu nome')

data_de_nascimento_do_usuario = verificacao_data_de_nascimento('sua data de nascimento')

status_usuário = voto(data_de_nascimento_do_usuario)

print(f'\no usuário {nome_usuario} {status_usuário}')
