# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

N = int(input('Введите количество элементов списка: '))
start = int(input('Введите диапазон значения чисел от: '))
finish = int(input('                                до: '))
my_list = []

# заполняем список
for i in range(N):
    my_list.append(randint(start, finish))

sum = 0
my_index = []
for i in range(N):
    if i % 2 != 0:
        sum += my_list[i]
        my_index.append(my_list[i])

print(f'{my_list} -> на нечётных позициях элементы ', end='')
print(*my_index, sep=' и ', end='')
print(f', ответ: {sum}')
