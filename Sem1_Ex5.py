# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
'''
#первоначальный код
import math
print('Введите координаты точки А')
AX=float(input('X='))
AY=float(input('Y='))
print('Введите координаты точки B')
BX=float(input('X='))
BY=float(input('Y='))
number=math.sqrt((BX-AX)**2+(BY-AY)**2)
print('Расстояние между двумя точками равно', round(number, 2))
'''
#изменения:
    #1. Единственное, что присвоение переменной убрала и сразу в вывод на печать засунула формулу. Ввод такой оставила для удобства пользователя

import math

# проверка ввода данных
def f_input(number):
    while True:
        try:
            int(number)
            break
        except ValueError:
            number = input('Введите ЧИСЛОВОЕ значение:')
    return number

print('Введите координаты точки А')
AX = int(f_input(input('X=')))
AY = int(f_input(input('Y=')))
print('Введите координаты точки B')
BX = int(f_input(input('X=')))
BY = int(f_input(input('Y=')))
print(f'Координаты точки А ({AX};{AY})\nКоординаты точки B ({BX};{BY})')
print('Расстояние между двумя точками равно',
    round(math.sqrt((BX-AX)**2+(BY-AY)**2), 2))