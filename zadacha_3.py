# Создайте программу для игры в ""Крестики-нолики"".

table = [[1,2,3],[4,5,6],[7,8,9]]
print(table)
for i in table:
    print(i)

player_1 = True

while True:
    if player_1:
        print('Игрок 1')
    else:
        print('Игрок 2')
    hod = int(input('Введите номер'))
