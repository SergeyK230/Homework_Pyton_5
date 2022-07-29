# Создайте программу для игры с конфетами человек против человека.
# 
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# 
# a) Добавьте игру против бота
# 
# b) Подумайте как наделить бота ""интеллектом""


def VS_Com_Player(candys = 2021):
    player1 = True
    while candys > 28:
        if player1:
            print('Игрок 1')
            hod = int(input('Введите количество конфет от 1 до 28 -> '))
            if 0 < hod < 29:
                candys -= hod
                print(candys)
                player1 = not player1
            else:
                print('Неправильный ввод')
        else:
            print('Компьютер')
            grab = candys % 28 - 1
            if grab == 0:
                grab = 28
            elif grab == -1:
                grab = 27
            print('Взял -> ', grab)
            candys -= grab
            print(candys)
            player1 = not player1
    if player1:
        print('Игрок 1 победил')
    else:
        print('Компьютер победил')
    
def VS_Humam(candys = 2021):    
    player1 = True
    while candys > 28:
        if player1:
            print('Игрок 1')
        else:
            print('Игрок 2')
        hod = int(input('Введите количество конфет от 1 до 28 -> '))
        if 0 < hod < 29:
            candys = candys - hod
            print(candys)
            player1 = not player1
        else:
            print('Неправильный ввод')

    if player1:
        print('Игрок 1 победил')
    else:
        print('Игрок 2 победил')

VS_Com_Player(200)
