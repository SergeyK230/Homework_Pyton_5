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

from random import randint
from secrets import choice


def Player(player_number, candys):
    print('Игрок ',player_number)
    while True:
        hod = int(input('Введите количество конфет от 1 до 28 -> '))
        if 0 < hod < 29:
            candys -= hod
            print(candys)
            break
        else:
            print('Неправильный ввод')
    return candys

def Com_Player(candys):
    print('Компьютер')
    grab = candys % 29
    if grab == 0:
        grab = randint(1,28)
    print('Взял -> ', grab)
    candys -= grab
    print(candys)

    return candys

def Game(player_coll = 1, candys = 2021):
    player_1 = choice([True, False])

    while candys > 28:
        if player_1:
            candys = Player(1, candys)
            player_1 = not player_1
        elif player_coll == 2:
            candys = Player(2,candys)
            player_1 = not player_1
        else:
            candys = Com_Player(candys)
            player_1 = not player_1

    if player_1:
        print('Игрок 1 победил')
    elif player_coll == 2:
        print('Игрок 2 победил')
    else:
        print('Компьютер победил')

coll = int(input('Введите количество игроков(1 или 2) -> '))
Game(coll, 2021)
