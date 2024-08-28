print('descubra a sua categoria')
user_year = int(input('digite o ano em que você nasceu: '))
age = 2024 - user_year
if age <= 9 and age >= 0:
    print('como você possui {} ano(s), sua categoria é a categoria MIRIM' .format(age))
else:
    if age > 9 and age <= 14:
        print('como você possui {} anos, sua categoria é a categoria INFANTIL' .format(age))
    else:
        if age > 14 and age <= 19:
            print('como você possui {} anos, sua categoria é a JUNIOR' .format(age))
        else:
            if age == 20:
                print('como você possui {} anos, sua categoria é a SÊNIOR' .format(age))
            else:
                if age > 20:
                    print('como você possui {} anos, sua categoria é a MASTER' .format(age))
print(' ')
print('boa sorte nas competições!')
