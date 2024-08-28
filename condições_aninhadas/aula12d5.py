print('calcule a sua média bimestral')
n1 = float(input('digite a nota da sua AV1: '))
n2 = float(input('digite a nota da sua AV2: '))
media = (n1 + n2) / 2
if media >= 7:
    print('parabéns, sua média de {:.1f} é suficiente para sua aprovação' .format(media))
else:
    if 5 <= media and media <= 6.9:
        print('ainda há esperança, mesmo com sua média de {:.1f} você ainda está na recuperação' .format(media))
    else:
        if media < 5 and media >= 0:
            print('lamento, mas sua média de {:.1f} não é suiciente nem para a recuperação. Te vejo ano que vem kkkkk' .format(media))
        else:
            if media < 0:
                print('ta expulso engraçadinho, vai fazeer gracinha na casa do carai')
print("""
""")
print('tenha um bom dia')
