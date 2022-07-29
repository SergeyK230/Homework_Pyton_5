# Создайте программу для игры в ""Крестики-нолики"".

def Game(table):
    player_1 = True
    win = False

    for number in range(9):
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
        for i in table:
            print(i)

        if number > 4:
            win = Check(table)
            if win:
                if player_1:
                    print('X Победил')
                    break
                else:
                    print('O Победил')
                    break
        player_1 = not player_1
        
    if not win:
        print('Ничья')

def Check(table):
    win = False
    if table[0][0] == table[0][1] == table[0][2]:
        win = True
    elif table[1][0] == table[1][1] == table[1][2]:
        win = True
    elif table[2][0] == table[2][1] == table[2][2]:
        win = True
    elif table[0][0] == table[1][0] == table[2][0]:
        win = True
    elif table[0][1] == table[1][1] == table[2][1]:
        win = True
    elif table[0][2] == table[1][2] == table[2][2]:
        win = True
    elif table[0][0] == table[1][1] == table[2][2]:
        win = True
    elif table[2][0] == table[1][1] == table[0][2]:
        win = True
    return win


table = [['1','2','3'],['4','5','6'],['7','8','9']]
for i in table:
    print(i)
Game(table)










