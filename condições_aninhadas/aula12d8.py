print('calculadora de IMC \n ')
weight = float(input('digite o seu peso em Kilogramas: '))
high = float(input('digite a sia altura em Metros: '))
print(' ')
IMC = weight / (high ** 2)
print('seu IMC é {:.1f} \n ' .format(IMC))
if IMC < 18.5:
    print('você está abixo do peso')
else:
    if IMC > 18.5 and IMC < 25:
        print('você está no seu peso ideal')
    else:
        if IMC >= 25 and IMC <= 30:
            print('você está com sobrapeso')
        else:
            if IMC > 30 and IMC <= 40:
                print('você possui obesidade')
            else:
                if IMC > 40:
                    print('e é a montanha é kkkkkkkkkkk')
