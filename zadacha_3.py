# Создайте программу для игры в ""Крестики-нолики"".

table = [['1','2','3'],['4','5','6'],['7','8','9']]
for i in table:
    print(i)

player_1 = True

while True:
    if player_1:
        print('Игрок X')
    else:
        print('Игрок O')
    hod = input('Введите номер-> ')
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == hod:
                if player_1:
                    table[i][j] = 'X'
                else:
                    table[i][j] = 'O'

    if table[0][0] == table[0][1] == table[0][2]:
        break
    elif table[1][0] == table[1][1] == table[1][2]:
        break
    elif table[2][0] == table[2][1] == table[2][2]:
        break
    elif table[0][0] == table[1][0] == table[2][0]:
        break
    elif table[0][1] == table[1][1] == table[2][1]:
        break
    elif table[0][2] == table[1][2] == table[2][2]:
        break
    elif table[0][0] == table[1][1] == table[2][2]:
        break
    elif table[2][0] == table[1][1] == table[0][2]:
        break
    for i in table:
        print(i)
    player_1 = not player_1
for i in table:
        print(i)
if player_1:
    print('X Победил')
else:
    print('O Победил')









