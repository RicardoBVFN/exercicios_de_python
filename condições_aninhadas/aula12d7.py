print('analisador trigonométrico 2.0 \n ')
l1 = float(input('digite o compriemnto do primeiro segmento: '))
l2 = float(input('digite o comprimento do segundo segmento: '))
l3 = float(input('digite o comprimento do terceiro segmento: '))
print(' ')
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('estes segmentos podem formar um triângulo \n ')
    if l1 == l2 and l1 == l3:
        print('esse triângulo é EQUILÁTERO')
    else:
        if l1 - l2 == 0 or l1 - l3 == 0 or l2 - l3 == 0:
            print('esse triângulo é ISÓCELES')
        else:
            print('esse triângulo é ESCALENO')
else:
    print('esses segmentos não podem compor um triângulo')
