# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

from random import randint

N = int(input('Введите количество элементов списка: '))
start = int(input('Введите диапазон значения чисел от: '))
finish = int(input('                               до: '))
my_list = []

for i in range(N):
    my_list.append(randint(start, finish))

my_new_list = []

if len(my_list) % 2 == 0:
    for i in range(N//2):
        my_new_list.append(my_list[i]*my_list[N-1-i])
else:
    for i in range(N//2+1):
        my_new_list.append(my_list[i]*my_list[N-1-i])

print(f'{my_list} => {my_new_list}')
