print('leitor de velocidade')
velocidade = int(input('digite a sua velocidade (em Km/h): '))
print("""
""")
if (velocidade > 80 and velocidade < 120) or velocidade < 40:
    print('você levou uma multa de R$293,47 além de 7 pontos na sua CNH')
else:
    if velocidade >= 120:
        print('você levou uma multa de R$293,47 , 7 pontos na sua CNH e está com a mesma sendo caçada ')
    else:
        print('ok, prossiga com cuidado')
