# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

'''
#первоначальный код
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
'''
from random import randint

# проверка ввода данных
def f_input(number):
    while True:
        try:
            int(number)
            break
        except ValueError:
            number = input('Введите ЧИСЛОВОЕ значение:')
    return number

N = int(f_input(input('Введите количество элементов списка: ')))
start = int(f_input(input('Введите диапазон значения чисел от: ')))
finish = int(f_input(input('\t\t\t\tдо: ')))

my_list = []

for i in range(N):
    my_list.append(randint(start, finish))

if len(my_list) % 2 == 0:
    my_new_list = list((my_list[i]*my_list[N-1-i]) for i in range(N//2))
else:
    my_new_list = list(my_list[i]*my_list[N-1-i] for i in range(N//2+1))

print(f'{my_list} => {my_new_list}')
