print('calculadora fatorial\n ')

n = int(input('digite o número a ser fatoriado: '))

fatoriando = n 
resposta = 0

while fatoriando != 0:

    fatoriando = fatoriando - 1

    if fatoriando == n - 1:
        resposta = n * fatoriando

    else:
        if fatoriando != 0:
            resposta = resposta * fatoriando
            
print ( resposta) 
    