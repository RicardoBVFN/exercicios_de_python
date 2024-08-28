nome_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze')
while True:
    user_input = int(input('digite um número inteiro de 0 a 15: '))
    if user_input >= 0 and user_input <= 15:
        break
    print('números fora do intervalo não serão tolerados, tente novamente')
print(f' \no número {user_input} escrito por extenso é: {nome_extenso[user_input]}')