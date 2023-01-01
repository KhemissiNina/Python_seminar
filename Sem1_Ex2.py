# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

X = int(input('Введите значение координаты Х, не равное 0: '))
Y = int(input('Введите значение координаты Y, не равное 0: '))
if X == 0 or Y == 0:
    print('Вы ввели нулевое  значение')
else:
    if X > 0 and Y > 0:
        print('Координаты лежат в 1-ой четверти')
    else:
        if X > 0 and Y < 0:
            print('Координаты лежат в 4-ой четверти')
        else:
            if X < 0 and Y > 0:
                print('Координаты лежат во 2-ой четверти')
            else:
                print('Координаты лежат в 3-ей четверти')