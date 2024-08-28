maior = 0
menor = 0
for c in range(0, 5):
    peso = float(input('digite o seu peso: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(' \no maior peso foi de {}Kg, e o menor foi de {}Kg' .format(maior, menor))