print('matrizes em python\n')

line_1 = [[], [], []]
line_2 = [[], [], []]
line_3 = [[], [], []]
cont = 0

for c in range(0, 9):

    if c >= 0 and c <= 2:
        user_input = int(input(f'digite o valor correspondente a linha 1, coluna {c + 1}: '))
        line_1[c].append(user_input)
        if c == 2:
            print()

    if c >= 3 and c <= 5:
        user_input = int(input(f'digite o valor correspondente a linha 2, coluna {c - 2}: '))
        line_2[c - 3].append(user_input)
        if c == 5:
            print()

    if c >= 6 and c <= 8:
        user_input = int(input(f'digite o valor correspondente a linha 3, coluna {c - 5}: '))
        line_3[c - 6].append(user_input)
        
print('\nsua matriz ficou assim:\n')
print(line_1[0], ' ', line_1[1], ' ', line_1[2])
print(line_2[0], ' ', line_2[1], ' ', line_2[2])
print(line_3[0], ' ', line_3[1], ' ', line_3[2])