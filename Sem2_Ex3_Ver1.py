# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование библиотеки Random для и получения случайного int

'''
#первоначальный код
from random import randint

N=int(input('Введите количество элементов списка: '))
start=int(input('Введите диапозон значения чисел от: '))
finish=int(input('                                до: '))
my_list = []

for i in range(N):
    my_list.append(randint(start, finish))
print ('Первоначальный массив:', end=' ')
for i in my_list:
    print(i, end=' ')
print ('')

for i in range(N):
    time_index=randint(0,N-1)
    b=my_list[i]
    my_list[i]=my_list[time_index]
    my_list[time_index]=b

print ('Перемешанный массив:  ', end=' ')
for i in my_list:
    print(i, end=' ')
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

print('Первоначальный массив: ', end=' ')
print(*my_list)

for i in range(N):
    time_index = randint(0, N-1)
    b = my_list[i]
    my_list[i] = my_list[time_index]
    my_list[time_index] = b

print('Перемешанный массив:   ', end=' ')
print(*my_list)
