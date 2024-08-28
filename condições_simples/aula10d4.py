print('calcule o custo da sua viagem')
print("""
""")
distance = float(input('digite a distância da sua viagem em kilômetros: '))
print("""
""")
if distance <= 200 and distance > 0:
    cost = distance * 0.5
    print('o custo da sua viagem será de R${}' .format(cost))
else:
    if distance < 0:
        print('valor inválido para uma viagem, comprimentos não podem ser negativos')
    else:
        cost = distance * 0.45
        print('o custo da sua viagem será de R${}' .format(cost))
