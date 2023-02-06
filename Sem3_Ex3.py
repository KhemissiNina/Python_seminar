# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

'''
#первоначальный код
from random import uniform

N = int(input('Введите количество элементов списка: '))
start = int(input('Введите диапазон значения чисел от: '))
finish = int(input('                                до: '))
my_list = []

for i in range(N):
    number = round(uniform(start, finish), 2)
    my_list.append(number)

# принудительно зададим целое число
my_list[3] = 5

max = 0.0
min = 0.99

for item in my_list:
    if item-int(item) != 0:
        if (item-int(item)) > max:
            max = round((item-int(item)), 2)
        if (item-int(item)) < min:
            min = round((item-int(item)), 2)
    else:
        continue

print('[', end='')
for i in range(N):
    if i == N-1:
        if my_list[i] == int(my_list[i]):
            print(f'{int(my_list[i])}] => {round((max-min),2)}')
        else:
            print(f'{(my_list[i])}] => {round((max-min),2)}')
    else:
        if my_list[i] == int(my_list[i]):
            print(int(my_list[i]), end=', ')
        else:
            print(my_list[i], end=', ')
'''
from random import uniform

# проверка ввода данных
def f_input(number):
    while True:
        try:
            float(number)
            break
        except ValueError:
            number = input('Введите ЧИСЛОВОЕ значение:')
    return number

N = int(f_input(input('Введите количество элементов списка: ')))
start = float(f_input(input('Введите диапазон значения чисел от: ')))
finish = float(f_input(input('\t\t\t\tдо: ')))

my_list = []

for i in range(N):
    number = round(uniform(start, finish), 2)
    my_list.append(number)

# принудительно зададим целое число
my_list[3] = 5

change_list = list(round((my_list[i]-int(my_list[i])), 2)
                   for i in range(len(my_list)))
change_list = list(filter(lambda item: item > 0, change_list))

print(my_list, '=>', round((max(change_list)-min(change_list)), 2))
